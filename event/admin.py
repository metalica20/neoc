from django.contrib import admin
from bipad.admin import GeoModelAdmin
from .models import Event


@admin.register(Event)
class EventAdmin(GeoModelAdmin):
    list_display = ['title', 'severity', 'created_on']
