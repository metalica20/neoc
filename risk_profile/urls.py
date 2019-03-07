from django.urls import path,include
from . import views

urlpatterns = [
    path('hospital',views.HospitalViewSet.as_view({'get':'list'}),name='hospital'),
    path('hospitaljson',views.HospitalGeojsonViewSet.as_view(),name='hospitaljson'),
    path('marketcenterjson',views.MarketCenterGeojsonViewSet.as_view(),name='marketcenterjson'),
]
