"""
BIPAD URL Configuration
"""
from django.conf import settings
from django.contrib import admin
from django.conf.urls import static
from django.urls import path, re_path, include
from rest_framework import routers
from rest_framework_simplejwt.views import (
    TokenObtainPairView,
    TokenRefreshView,
    TokenVerifyView,
)
from hazard.views import HazardViewSet
from alert.views import AlertViewSet
from incident.views import IncidentViewSet
from event.views import EventViewSet
from federal.views import (
    ProvinceViewSet,
    DistrictViewSet,
    MunicipalityViewSet,
    WardViewSet,
)
from resources.views import ResourceViewSet
from organization.views import (
    OrganizationViewSet,
    ProjectViewSet,
)
from loss.views import (
    SimpleLossViewSet,
    InfrastructureTypeViewSet,
    LivestockTypeViewSet,
)

admin.site.site_header = 'BIPAD administration'

router = routers.DefaultRouter()
router.register(r'hazard', HazardViewSet,
                base_name='hazard')
router.register(r'alert', AlertViewSet,
                base_name='alert')
router.register(r'incident', IncidentViewSet,
                base_name='incident')
router.register(r'event', EventViewSet,
                base_name='event')
router.register(r'province', ProvinceViewSet,
                base_name='province')
router.register(r'district', DistrictViewSet,
                base_name='district')
router.register(r'municipality', MunicipalityViewSet,
                base_name='municipality')
router.register(r'ward', WardViewSet,
                base_name='ward')
router.register(r'resource', ResourceViewSet,
                base_name='resource')
router.register(r'organization', OrganizationViewSet,
                base_name='organization')
router.register(r'project', ProjectViewSet,
                base_name='project')
router.register(r'loss', SimpleLossViewSet,
                base_name='loss')
router.register(r'infrastructure-type', InfrastructureTypeViewSet,
                base_name='infrastructure_type')
router.register(r'livestock-type', LivestockTypeViewSet,
                base_name='livestock_type')

API_VERSION = 'v1'


def get_api_path(path):
    return r'^api/(?P<version>({}))/{}'.format(API_VERSION, path)


urlpatterns = [
    path('admin/', admin.site.urls),
    path('api-auth/', include('rest_framework.urls')),
    re_path(get_api_path(r'token/$'), TokenObtainPairView.as_view(),
            name='token_obtain_pair'),
    re_path(get_api_path(r'token/refresh/$'),
            TokenRefreshView.as_view(), name='token_refresh'),
    re_path(get_api_path(r'token/verify/$'),
            TokenVerifyView.as_view(), name='token_verify'),
    re_path(get_api_path(''), include(router.urls)),
] + static.static(
    settings.MEDIA_URL,
    document_root=settings.MEDIA_ROOT
)
