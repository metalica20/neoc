from django.contrib import admin
from .models import Incident,IncidentSource
from bipad.admin import GeoModelAdmin

admin.site.register(Incident, GeoModelAdmin)
admin.site.register(IncidentSource, GeoModelAdmin)
