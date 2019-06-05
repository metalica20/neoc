from django.contrib import admin
from .models import LayerTable,Health,MunicipalityLevelVulnerability,DistrictLevelVulnerability,Hydropower,HazardType,HazardLayer,HazardSubLayer,ExposureType,ExposureLayer
# Register your models here.
admin.site.register(Hydropower)
admin.site.register(HazardType)
admin.site.register(LayerTable)
admin.site.register(HazardLayer)
admin.site.register(HazardSubLayer)
# admin.site.register(HazardSubLayerDetail)
#admin.site.register(Bridge)
admin.site.register(MunicipalityLevelVulnerability)
admin.site.register(ExposureType)
admin.site.register(ExposureLayer)
admin.site.register(Health)
admin.site.register(DistrictLevelVulnerability)
# admin.site.register(ExposureLayerDetail)
