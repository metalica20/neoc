from django.contrib import admin
from bipad.admin import GeoModelAdmin
from .models import Alert


@admin.register(Alert)
class AlertAdmin(GeoModelAdmin):
    exclude = ('wards',)
