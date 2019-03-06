from django.urls import path
from . import views

urlpatterns = [
    path('hazard-resource/<str:hazard>/<str:lat>/<str:long>/',views.HazardResourceViewSet.as_view(),name='hazard-resource'),
    path('hazard-resource/<str:hazard>/<str:lat>/<str:long>/distance/<str:distance>',views.HazardResourceViewSet.as_view(),name='hazard-resource'),
    path('hazard-resource/<str:hazard>/<str:lat>/<str:long>/count/<str:count>',views.HazardResourceViewSet.as_view(),name='hazard-resource'),
    path('hazard-resource/<str:hazard>/<str:lat>/<str:long>/distance/<str:distance>/count/<str:count>',views.HazardResourceViewSet.as_view(),name='hazard-resource'),

]
