from django.contrib import admin
from .models import Incident
from bipad.admin import GeoModelAdmin

admin.site.register(Incident, GeoModelAdmin)
