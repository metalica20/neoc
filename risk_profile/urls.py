from django.urls import path,include
from . import views

urlpatterns = [
    path('layer',views.LayerViewset.as_view({'get':'list'}),name='layer'),
    path('hospitaljson',views.HospitalGeojsonViewSet.as_view(),name='hospitaljson'),
    path('marketcenterjson',views.MarketCenterGeojsonViewSet.as_view(),name='marketcenterjson'),
    # path('hospital',views.LayerViewset.as_view({'get':'list'}),name='hospital'),
]
