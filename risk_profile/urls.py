from django.urls import path,include
from . import views

urlpatterns = [
    path('Layer',views.LayerViewset.as_view({'get':'list'}),name='Layer'),
    path('sociocook',views.SociocookViewSet.as_view({'get':'list'}),name='sociocook'),
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
    path('Health',views.HealthGeojsonViewSet.as_view(),name='Health'),
    path('Newfile/<str:field>',views.NewtestfileViewSet.as_view(),name='Newfile'),
    path('Flood',views.HazardfloodViewSet.as_view(),name='Flood'),
    path('Earthquake',views.EarthquakefloodViewSet.as_view(),name='Earthquake'),
    # path('Risk',views.RiskApiView.as_view({'get':'list'}),name='Risk'),
    path('Risk',views.RiskApiView.as_view(),name='Risk'),
    # path('hospital',views.LayerViewset.as_view({'get':'list'}),name='hospital'),
]
