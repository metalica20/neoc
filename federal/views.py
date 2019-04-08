from django.conf import settings
from django.contrib.gis.db.models.functions import Centroid
from django.contrib.gis.db.models import Extent
from django.utils.decorators import method_decorator
from django.views.decorators.cache import cache_control
from .renderer import GeoJSONRenderer
from rest_framework.renderers import (
    JSONRenderer,
    BrowsableAPIRenderer,
)
from rest_flex_fields import (
    FlexFieldsModelViewSet,
    is_expanded,
)
from .serializers import (
    ProvinceSerializer,
    ProvinceGeoSerializer,
    DistrictSerializer,
    DistrictGeoSerializer,
    MunicipalitySerializer,
    MunicipalityGeoSerializer,
    WardSerializer,
    WardGeoSerializer,
)
from .models import (
    Province,
    District,
    Municipality,
    Ward,
)
from .filters import WardFilter


class ProvinceViewSet(FlexFieldsModelViewSet):
    renderer_classes = (JSONRenderer, GeoJSONRenderer, BrowsableAPIRenderer)
    search_fields = ('title',)
    queryset = Province.objects.annotate(
        bbox=Extent('boundary'),
        centroid=Centroid('boundary'),
    ).all()

    def get_serializer_class(self):
        # TODO: fix me
        format = self.request.query_params.get('format')
        if format == 'geojson':
            return ProvinceGeoSerializer
        return ProvinceSerializer

    @method_decorator(cache_control(public=True, max_age=settings.FEDERAL_CACHE_CONTROL_MAX_AGE))
    def dispatch(self, request, *args, **kwargs):
        return super().dispatch(request, *args, **kwargs)


class DistrictViewSet(FlexFieldsModelViewSet):
    renderer_classes = (JSONRenderer, GeoJSONRenderer, BrowsableAPIRenderer)
    search_fields = ('title',)
    filter_fields = ('province',)
    permit_list_expands = ['province']

    def get_queryset(self):
        queryset = District.objects.annotate(
            bbox=Extent('boundary'),
            centroid=Centroid('boundary'),
        ).all()
        if is_expanded(self.request, 'province'):
            queryset = queryset.select_related('province')
        return queryset

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
    renderer_classes = (JSONRenderer, GeoJSONRenderer, BrowsableAPIRenderer)
    search_fields = ('title',)
    filter_fields = ('district',)
    permit_list_expands = ['district', 'province']

    def get_queryset(self):
        queryset = Municipality.objects.annotate(
            bbox=Extent('boundary'),
            centroid=Centroid('boundary'),
        ).all()
        if is_expanded(self.request, 'district'):
            queryset = queryset.select_related('district')
        if is_expanded(self.request, 'province'):
            queryset = queryset.select_related('district__province')
        return queryset

    def get_serializer_class(self):
        # TODO: fix me
        format = self.request.query_params.get('format')
        if format == 'geojson':
            return MunicipalityGeoSerializer
        return MunicipalitySerializer

    @method_decorator(cache_control(public=True, max_age=settings.FEDERAL_CACHE_CONTROL_MAX_AGE))
    def dispatch(self, request, *args, **kwargs):
        return super().dispatch(request, *args, **kwargs)


class WardViewSet(FlexFieldsModelViewSet):
    renderer_classes = (JSONRenderer, GeoJSONRenderer, BrowsableAPIRenderer)
    search_fields = ('title', 'municipality__title')
    filter_class = WardFilter
    permit_list_expands = ['municipality', 'district', 'province']

    def get_queryset(self):
        queryset = Ward.objects.annotate(
            bbox=Extent('boundary'),
            centroid=Centroid('boundary'),
        ).all()
        if is_expanded(self.request, 'municipality'):
            queryset = queryset.select_related('municipality')
        if is_expanded(self.request, 'district'):
            queryset = queryset.select_related('municipality__district')
        if is_expanded(self.request, 'province'):
            queryset = queryset.select_related('municipality__district__province')
        return queryset

    def get_serializer_class(self):
        # TODO: fix me
        format = self.request.query_params.get('format')
        if format == 'geojson':
            return WardGeoSerializer
        return WardSerializer

    @method_decorator(cache_control(public=True, max_age=settings.FEDERAL_CACHE_CONTROL_MAX_AGE))
    def dispatch(self, request, *args, **kwargs):
        return super().dispatch(request, *args, **kwargs)
