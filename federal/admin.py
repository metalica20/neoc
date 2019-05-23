from django.contrib import admin
from .models import (
    Province,
    District,
    Municipality,
    Ward,
)
from bipad.admin import GeoModelAdmin


@admin.register(Municipality)
class MunicipalityAdmin(GeoModelAdmin):
    list_display = ('title', 'district')
    search_fields = ('title',)


@admin.register(District)
class DistrictAdmin(GeoModelAdmin):
    list_display = ('title', 'province')
    search_fields = ('title',)


@admin.register(Ward)
class WardAdmin(GeoModelAdmin):
    search_fields = ('title',)


admin.site.register(Province, GeoModelAdmin)
