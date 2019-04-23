import json
from django.contrib import (
    admin,
    messages,
)
from bipad.admin import GeoModelAdmin
from .models import Alert
from .utils import (
    get_similar_alerts,
    generate_polygon_from_wards,
    get_alert_title
)
from django.utils.safestring import mark_safe
from django.contrib.gis.geos import GEOSGeometry
from django import forms
from misc.validators import validate_geojson
from django_select2.forms import (
    ModelSelect2Widget,
    ModelSelect2MultipleWidget,
)
from federal.models import (
    District,
    Municipality,
    Ward
)


class AlertForm(forms.ModelForm):
    def __init__(self, *args, **kwargs):
        instance = kwargs.get('instance', None)
        super(AlertForm, self).__init__(*args, **kwargs)
        if instance:
            wards = Alert.objects.values('wards').filter(id=instance.id)
            if wards[0]['wards']:
                municipality = Ward.objects.values(
                    'municipality',
                    'municipality__district'
                ).filter(id=wards[0]['wards'])
                self.fields['municipality'].initial = municipality[0]['municipality']
                self.fields['district'].initial = municipality[0]['municipality__district']
    geojson = forms.FileField(
        required=False,
        validators=[validate_geojson],
    )

    district = forms.ModelChoiceField(
        queryset=District.objects.all(),
        required=False,
        widget=ModelSelect2Widget(
            model=District,
            search_fields=['title__icontains'],
        )
    )

    municipality = forms.ModelChoiceField(
        queryset=Municipality.objects.all(),
        required=False,
        widget=ModelSelect2Widget(
            model=Municipality,
            search_fields=['title__icontains'],
            dependent_fields={'district': 'district'},
        )
    )

    wards = forms.ModelMultipleChoiceField(
        queryset=Ward.objects.all(),
        required=False,
        widget=ModelSelect2MultipleWidget(
            model=Ward,
            search_fields=['title__icontains'],
            dependent_fields={'municipality': 'municipality'},
        )
    )

    class Meta:
        model = Alert
        fields = (
            'source',
            'description',
            'verified',
            'public',
            'hazard',
            'started_on',
            'expire_on',
            'event',
            'district',
            'municipality',
            'wards',
            'point',
            'geojson',
            'polygon',
        )


@admin.register(Alert)
class AlertAdmin(GeoModelAdmin):

    search_fields = ('title', 'started_on', 'wards__title', 'wards__municipality__title',
                     'wards__municipality__district__title', 'hazard__title',)
    list_display = ('title', 'source', 'verified', 'public', 'started_on', 'expire_on', 'hazard',)
    exclude = ('title',)
    form = AlertForm

    def save_model(self, request, obj, form, change):

        geojson = form.cleaned_data.get('geojson')
        wards = form.cleaned_data.get('wards')

        # geojson takes precedence over others
        if geojson:
            geojson = json.loads(geojson.read().decode('utf-8'))
            # override polygon from geojson
            obj.polygon = GEOSGeometry(json.dumps(geojson['geometry']))

        if obj.polygon:
            # polygon overrides wards
            wards = Ward.objects.filter(boundary__intersects=obj.polygon)
            form.cleaned_data['wards'] = wards

        if wards and not obj.polygon:
            obj.polygon = generate_polygon_from_wards(wards)
            # generate centroid from polygon
        if not obj.point and obj.polygon:
            obj.point = GEOSGeometry(obj.polygon).centroid

        obj.title = get_alert_title(obj)
        super(AlertAdmin, self).save_model(request, obj, form, change)
        similar_alerts = get_similar_alerts(obj)
        for alert in similar_alerts:
            messages.add_message(request, messages.INFO, mark_safe(
                "Similar alert <a href='/admin/alert/alert/%d/change/'>%s</a> already exists"
                % (alert.id, alert.title)
            ))
