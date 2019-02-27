from rest_framework import viewsets
from .renderer import GeoJSONRenderer
from rest_framework.renderers import (
    JSONRenderer,
    BrowsableAPIRenderer,
)
from .serializers import (
    ProvinceSerializer,
    DistrictSerializer,
    DistrictGeoSerializer,
    MunicipalitySerializer,
    WardSerializer,
)
from .models import (
    Province,
    District,
    Municipality,
    Ward,
)


class ProvinceViewSet(viewsets.ModelViewSet):
    serializer_class = ProvinceSerializer
    search_fields = ('title',)
    queryset = Province.objects.all()


class DistrictViewSet(viewsets.ModelViewSet):
    serializer_class = DistrictSerializer
    renderer_classes = (JSONRenderer, GeoJSONRenderer, BrowsableAPIRenderer)
    search_fields = ('title',)
    filter_fields = ('province',)
    queryset = District.objects.all()

    def get_serializer_class(self):
        # TODO: fix me
        format = self.request.query_params.get('format')
        if format == 'geojson':
            return DistrictGeoSerializer
        return DistrictSerializer


class MunicipalityViewSet(viewsets.ModelViewSet):
    serializer_class = MunicipalitySerializer
    search_fields = ('title',)
    filter_fields = ('district',)
    queryset = Municipality.objects.all()


class WardViewSet(viewsets.ModelViewSet):
    serializer_class = WardSerializer
    search_fields = ('title',)
    filter_fields = ('municipality',)
    queryset = Ward.objects.all()
