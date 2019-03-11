from django.contrib import admin
from bipad.admin import GeoModelAdmin
from .models import Incident


@admin.register(Incident)
class IncidentAdmin(GeoModelAdmin):
    search_fields = ('title', 'description', 'street_address', 'hazard__title')
    list_display = ('title', 'hazard', 'source', 'incident_on')
    list_filter = ('verified', 'hazard', 'source', 'inducer')
    autocomplete_fields = ['wards']
    raw_id_fields = ('loss',)
    exclude = ['detail']
