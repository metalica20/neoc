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


@admin.register(District)
class DistrictAdmin(GeoModelAdmin):
    list_display = ('title', 'province')


admin.site.register([Province, Ward], GeoModelAdmin)


