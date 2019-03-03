from rest_framework import viewsets
from .serializers import (
    LossSerializer,
    InfrastructureTypeSerializer,
    LivestockTypeSerializer
)
from .models import (
    Loss,
    InfrastructureType,
    LivestockType
)


class LossViewSet(viewsets.ModelViewSet):
    serializer_class = LossSerializer
    queryset = Loss.with_stat.all()


class InfrastructureTypeViewSet(viewsets.ModelViewSet):
    serializer_class = InfrastructureTypeSerializer
    queryset = InfrastructureType.objects.all()


class LivestockTypeViewSet(viewsets.ModelViewSet):
    serializer_class = LivestockTypeSerializer
    queryset = LivestockType.objects.all()
