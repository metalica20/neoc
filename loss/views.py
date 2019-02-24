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
from bipad.models import DistinctSum
from django.db.models import Q
from django.db.models.functions import Coalesce


class SimpleLossViewSet(viewsets.ModelViewSet):
    serializer_class = SimpleLossSerializer
    queryset = Loss.objects.annotate(
        people_death_count=Coalesce(DistinctSum(
            'peoples__count',
            filter=Q(peoples__status='dead')
        ), 0),
        livestock_destroyed_count=Coalesce(DistinctSum(
            'livestocks__count',
            filter=Q(livestocks__status='destroyed')
        ), 0),
        infrastructure_destroyed_count=Coalesce(DistinctSum(
            'infrastructures__count',
            filter=Q(infrastructures__status='destroyed')
        ), 0),
    )


class InfrastructureTypeViewSet(viewsets.ModelViewSet):
    serializer_class = InfrastructureTypeSerializer
    queryset = InfrastructureType.objects.all()


class LivestockTypeViewSet(viewsets.ModelViewSet):
    serializer_class = LivestockTypeSerializer
    queryset = LivestockType.objects.all()
