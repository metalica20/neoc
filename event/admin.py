import re
import json
from django.contrib import (
    admin,
    messages
)
from bipad.admin import GeoModelAdmin
from .models import Event
from django import forms
from incident.models import Incident
from django_select2.forms import ModelSelect2MultipleWidget
from django.utils.translation import ugettext_lazy as _
from django.http import HttpResponseRedirect
from django.contrib.gis.geos import GEOSGeometry
from misc.validators import validate_geojson


class EventForm(forms.ModelForm):
    def __init__(self, *args, **kwargs):
        instance = kwargs.get('instance', None)
        super(EventForm, self).__init__(*args, **kwargs)
        if self.parameter:
            incident_id = re.findall(r'\d+', self.parameter)
            self.fields['incidents'].initial = Incident.objects.filter(id__in=incident_id)
        if instance:
            incidents = Incident.objects.filter(event=instance)
            self.fields['incidents'].initial = incidents

    incidents = forms.ModelMultipleChoiceField(
        queryset=Incident.objects.all(),
        required=False,
        label=_("Incident"),
        widget=ModelSelect2MultipleWidget(
            model=Incident,
            search_fields=['title__icontains'],
        )
    )

    geojson = forms.FileField(
        required=False,
        validators=[validate_geojson],
    )

    class Meta:
        model = Event
        fields = '__all__'


@admin.register(Event)
class EventAdmin(GeoModelAdmin):
    search_fields = ('title',)
    list_filter = ('severity',)
    list_display = ('title', 'started_on', 'ended_on', 'severity')
    actions = ("create_event",)
    form = EventForm

    class Media:
        css = {
            'all': ('federal/css/django_select2.css',)
        }

    def save_model(self, request, obj, form, change):
        geojson = form.cleaned_data.get('geojson')
        if geojson:
            geojson = json.loads(geojson.read().decode('utf-8'))
            obj.polygon = GEOSGeometry(json.dumps(geojson['geometry']))
        if not obj.point and obj.polygon:
            obj.point = GEOSGeometry(obj.polygon).centroid
        incidents = form.cleaned_data.get('incidents')
        super(EventAdmin, self).save_model(request, obj, form, change)
        for incident in incidents:
            Incident.objects.filter(pk=incident.id).update(event=obj)

    def get_form(self, request, obj=None, **kwargs):
        form = super().get_form(request, obj, **kwargs)
        form.parameter = request.GET.get('incident')
        return form

    def create_event(self, request, queryset):
        if len(queryset) > 1:
            messages.add_message(
                request, messages.INFO,
                'Select only one event'
            )
            return
        event_id = queryset[0].id
        return HttpResponseRedirect('/admin/alert/alert/add/?event=%s' % event_id)

    create_event.short_description = 'Create Alert'
