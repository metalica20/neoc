from django.contrib import admin
from .models import LayerTable,Health,SocioEconomicGapanapa,Risk,Hydropower,HazardType,HazardLayer,HazardSubLayer,HazardSubLayerDetail
# Register your models here.
admin.site.register(Hydropower)
admin.site.register(HazardType)
admin.site.register(LayerTable)
admin.site.register(HazardLayer)
admin.site.register(HazardSubLayer)
admin.site.register(HazardSubLayerDetail)
#admin.site.register(Bridge)
admin.site.register(SocioEconomicGapanapa)
# admin.site.register(Education)
#admin.site.register(Settlements)
admin.site.register(Health)
admin.site.register(Risk)
# admin.site.register(Testw)
