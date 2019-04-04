import re
from django.contrib import admin
from bipad.admin import GeoModelAdmin
from .models import Event
from django import forms
from incident.models import Incident
from django_select2.forms import ModelSelect2MultipleWidget


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
        widget=ModelSelect2MultipleWidget(
            model=Incident,
            search_fields=['title__icontains'],
        )
    )

    class Meta:
        model = Event
        fields = '__all__'


@admin.register(Event)
class EventAdmin(GeoModelAdmin):
    form = EventForm

    class Media:
        css = {
            'all': ('federal/css/django_select2.css',)
        }

    def save_model(self, request, obj, form, change):
        incidents = form.cleaned_data.get('incidents')
        super(EventAdmin, self).save_model(request, obj, form, change)
        for incident in incidents:
            Incident.objects.filter(pk=incident.id).update(event=obj)

    def get_form(self, request, obj=None, **kwargs):
        form = super().get_form(request, obj, **kwargs)
        form.parameter = request.GET.get('incident')
        return form

