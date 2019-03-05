from rest_framework import viewsets
from .serializers import (
    SimpleLossSerializer,
    InfrastructureTypeSerializer,
    LivestockTypeSerializer
)
from .models import (
    Loss,
    InfrastructureType,
    LivestockType
)


class SimpleLossViewSet(viewsets.ModelViewSet):
    serializer_class = SimpleLossSerializer
    queryset = Loss.with_stat.all()


class InfrastructureTypeViewSet(viewsets.ModelViewSet):
    serializer_class = InfrastructureTypeSerializer
    queryset = InfrastructureType.objects.all()


class LivestockTypeViewSet(viewsets.ModelViewSet):
    serializer_class = LivestockTypeSerializer
    queryset = LivestockType.objects.all()
