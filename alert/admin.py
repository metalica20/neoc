import json
from django.contrib import (
    admin,
    messages,
)
from bipad.admin import GeoModelAdmin
from .models import Alert
from .utils import get_similar_alerts
from django.utils.safestring import mark_safe
from django.contrib.gis.geos import GEOSGeometry
from django import forms
from misc.validators import validate_geojson


class AlertForm(forms.ModelForm):
    geojson = forms.FileField(
        required=False,
        validators=[validate_geojson],
    )


@admin.register(Alert)
class AlertAdmin(GeoModelAdmin):
    search_fields = ('title', 'started_on', 'wards__title', 'wards__municipality__title',
                     'wards__municipality__district__title', 'hazard__title',)
    list_display = ('title', 'source', 'verified', 'public', 'started_on', 'expire_on', 'hazard',)
    exclude = ('wards',)
    form = AlertForm

    def save_model(self, request, obj, form, change):
        geojson = form.cleaned_data.get('geojson')
        if geojson:
            geojson = json.loads(geojson.read().decode('utf-8'))
            obj.polygon = GEOSGeometry(json.dumps(geojson['geometry']))
        if not obj.point and obj.polygon:
            obj.point = GEOSGeometry(obj.polygon).centroid

        super(AlertAdmin, self).save_model(request, obj, form, change)
        similar_alerts = get_similar_alerts(obj)
        for alert in similar_alerts:
            messages.add_message(request, messages.INFO, mark_safe(
                "Similar alert <a href='/admin/alert/alert/%d/change/'>%s</a> already exists"
                % (alert.id, alert.title)
            ))