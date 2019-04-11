from django.urls import path
from . import views

urlpatterns = [
    path('hazard-resource/<str:hazard>/<str:lat>/<str:long>/',views.HazardResourceViewSet.as_view(),name='hazard-resource'),
    path('hazard-resource/<str:hazard>/<str:lat>/<str:long>/distance/<str:distance>',views.HazardResourceViewSet.as_view(),name='hazard-resource'),
    path('hazard-resource/<str:hazard>/<str:lat>/<str:long>/distance/<str:distance>/count/<str:count>',views.HazardResourceViewSet.as_view(),name='hazard-resource'),
    path('mappage',views.MapPage.as_view(),name="mappage"),
    path('hazard-resources/', views.HazardResourceViewSetView.as_view({'get': 'list'}), name='hazard_resources'),

]
