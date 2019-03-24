from django.conf import settings
from django.contrib.gis.db.models import Extent
from django.utils.decorators import method_decorator
from django.views.decorators.cache import cache_control
from .renderer import GeoJSONRenderer
from rest_framework.renderers import (
    JSONRenderer,
    BrowsableAPIRenderer,
)
from rest_flex_fields import FlexFieldsModelViewSet
from .serializers import (
    ProvinceSerializer,
    DistrictSerializer,
    DistrictGeoSerializer,
    MunicipalitySerializer,
    WardSerializer,
    WardGeoSerializer,
)
from .models import (
    Province,
    District,
    Municipality,
    Ward,
)


class ProvinceViewSet(FlexFieldsModelViewSet):
    serializer_class = ProvinceSerializer
    search_fields = ('title',)
    queryset = Province.objects.annotate(bbox=Extent('boundary')).all()

    @method_decorator(cache_control(public=True, max_age=settings.FEDERAL_CACHE_CONTROL_MAX_AGE))
    def dispatch(self, request, *args, **kwargs):
        return super().dispatch(request, *args, **kwargs)


class DistrictViewSet(FlexFieldsModelViewSet):
    renderer_classes = (JSONRenderer, GeoJSONRenderer, BrowsableAPIRenderer)
    search_fields = ('title',)
    filter_fields = ('province',)
    queryset = District.objects.annotate(bbox=Extent('boundary')).all()
    permit_list_expands = ['province']

    def get_serializer_class(self):
        # TODO: fix me
        format = self.request.query_params.get('format')
        if format == 'geojson':
            return DistrictGeoSerializer
        return DistrictSerializer

    @method_decorator(cache_control(public=True, max_age=settings.FEDERAL_CACHE_CONTROL_MAX_AGE))
    def dispatch(self, request, *args, **kwargs):
        return super().dispatch(request, *args, **kwargs)


class MunicipalityViewSet(FlexFieldsModelViewSet):
    serializer_class = MunicipalitySerializer
    search_fields = ('title',)
    filter_fields = ('district',)
    queryset = Municipality.objects.annotate(bbox=Extent('boundary')).all()
    permit_list_expands = ['district', 'province']

    @method_decorator(cache_control(public=True, max_age=settings.FEDERAL_CACHE_CONTROL_MAX_AGE))
    def dispatch(self, request, *args, **kwargs):
        return super().dispatch(request, *args, **kwargs)


class WardViewSet(FlexFieldsModelViewSet):
    renderer_classes = (JSONRenderer, GeoJSONRenderer, BrowsableAPIRenderer)
    search_fields = ('title',)
    filter_fields = (
        'municipality',
        'municipality__district',
        'municipality__district__province',
    )
    queryset = Ward.objects.annotate(bbox=Extent('boundary')).all()
    permit_list_expands = ['municipality', 'district', 'province']

    def get_serializer_class(self):
        # TODO: fix me
        format = self.request.query_params.get('format')
        if format == 'geojson':
            return WardGeoSerializer
        return WardSerializer

    @method_decorator(cache_control(public=True, max_age=settings.FEDERAL_CACHE_CONTROL_MAX_AGE))
    def dispatch(self, request, *args, **kwargs):
        return super().dispatch(request, *args, **kwargs)
