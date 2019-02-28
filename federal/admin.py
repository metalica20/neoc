from django.contrib import admin
from .models import (
    Province,
    District,
    Municipality,
    Ward,
)
from bipad.admin import GeoModelAdmin

admin.site.register([Province, District, Municipality, Ward], GeoModelAdmin)
