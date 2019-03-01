from django.contrib import admin
from bipad.admin import GeoModelAdmin
from .models import Alert


admin.site.register(Alert, GeoModelAdmin)
