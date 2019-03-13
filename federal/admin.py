from django.contrib import admin
from .models import (
    Province,
    District,
    Municipality,
    Ward,
)
from bipad.admin import GeoModelAdmin


@admin.register(Ward)
class WardAdmin(GeoModelAdmin):
    search_fields = Ward.autocomplete_search_fields()


admin.site.register([Province, District, Municipality], GeoModelAdmin)
