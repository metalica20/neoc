from django.urls import path,include
from . import views

urlpatterns = [
    path('Layer',views.LayerViewset.as_view({'get':'list'}),name='Layer'),
    path('Hospital',views.HospitalGeojsonViewSet.as_view(),name='hospitaljson'),
    path('Marketcenter',views.MarketCenterGeojsonViewSet.as_view(),name='marketcenterjson'),
    path('Airport',views.AirportGeojsonViewSet.as_view(),name='airportjson'),
    path('Bridge',views.BridgeGeojsonViewSet.as_view(),name='bridgejson'),
    path('Policestation',views.PoliceGeojsonViewSet.as_view(),name='policejson'),
    path('Education',views.EducationGeojsonViewSet.as_view(),name='education'),
    path('Bank',views.BankGeojsonViewSet.as_view(),name='bank'),
    path('Settlements',views.SettlementsGeojsonViewSet.as_view(),name='settlements'),
    path('Dashboard',views.Dashboard,name='dashboard'),
    path('hazard-resource',views.SchoolViewSet.as_view({'get':'list'}),name='hazard-resources'),
    # path('hospital',views.LayerViewset.as_view({'get':'list'}),name='hospital'),
]
