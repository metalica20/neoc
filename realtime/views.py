from django.utils import timezone
from rest_framework import viewsets
from .serializers import (
    EarthquakeSerializer,
    RiverSerializer,
    RainSerializer,
)
from .models import (
    Earthquake,
    River,
    Rain,
)


class EarthquakeViewSet(viewsets.ModelViewSet):
    serializer_class = EarthquakeSerializer
    search_fields = ('title',)
    filter_fields = ('magnitude',)
    queryset = Earthquake.objects.all()


class RiverViewSet(viewsets.ModelViewSet):
    serializer_class = RiverSerializer
    search_fields = ('title', 'basin',)
    filter_fields = ('danger_level', 'warning_level', 'water_level_value')
    queryset = River.objects.all()


class RainViewSet(viewsets.ModelViewSet):
    serializer_class = RainSerializer
    search_fields = ('title', 'basin',)
    filter_fields = ('elevation', 'district',)
    queryset = Rain.objects.all()
