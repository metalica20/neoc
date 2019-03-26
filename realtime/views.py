from rest_framework import viewsets
from .filter_sets import (
    RiverFilter,
    RainFilter,
    EarthquakeFilter,
)
from .serializers import (
    EarthquakeSerializer,
    RiverSerializer,
    RainSerializer,
    PollutionSerializer,
)
from .models import (
    Earthquake,
    River,
    Rain,
    Pollution,
)


class EarthquakeViewSet(viewsets.ModelViewSet):
    serializer_class = EarthquakeSerializer
    filter_class = EarthquakeFilter
    search_fields = ('title', 'address')
    queryset = Earthquake.objects.all()


class RiverViewSet(viewsets.ModelViewSet):
    serializer_class = RiverSerializer
    filter_class = RiverFilter
    search_fields = ('title', 'basin')
    queryset = River.objects.all()


class RainViewSet(viewsets.ModelViewSet):
    serializer_class = RainSerializer
    filter_class = RainFilter
    search_fields = ('title', 'basin')
    queryset = Rain.objects.all()


class PollutionViewSet(viewsets.ModelViewSet):
    serializer_class = PollutionSerializer
    search_fields =('location',)
    queryset = Pollution.objects.all()
