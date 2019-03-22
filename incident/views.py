from rest_framework.decorators import action
from rest_framework.response import Response
from django.db.models import Prefetch
from rest_flex_fields import (
        FlexFieldsModelViewSet,
        is_expanded,
        )
from .serializers import IncidentSerializer
from resources.models import Resource
from resources.serializers import (
        ResponseSerializer,
        DetailResponseSerializer,
        )
from .models import Incident
from .filter_set import IncidentFilter
from loss.models import Loss

from django.contrib.gis.db.models.functions import Distance
from django.contrib.gis.measure import D


class IncidentViewSet(FlexFieldsModelViewSet):
    serializer_class = IncidentSerializer
    filter_class = IncidentFilter
    search_fields = ('title', )
    queryset = Incident.objects.filter(verified=True)\
        .prefetch_related(Prefetch('loss', queryset=Loss.with_stat.all()))
    permit_list_expands = [
        'event',
        'hazard',
        'wards',
        'loss',
        'loss.peoples',
        'loss.families',
        'loss.livestocks',
        'loss.infrastructures'
    ]

    def get_queryset(self):
        # TODO: research why wards are queried by default
        queryset = Incident.objects.filter(verified=True).prefetch_related('wards')
        loss_queryset = Loss.with_stat.all()
        if is_expanded(self.request, 'event'):
            queryset = queryset.select_related('event')
        if is_expanded(self.request, 'hazard'):
            queryset = queryset.select_related('hazard')
        if is_expanded(self.request, 'peoples'):
            loss_queryset = loss_queryset.prefetch_related('peoples')
        if is_expanded(self.request, 'families'):
            loss_queryset = loss_queryset.prefetch_related('families')
        if is_expanded(self.request, 'livestocks'):
            loss_queryset = loss_queryset.prefetch_related('livestocks')
        if is_expanded(self.request, 'infrastructures'):
            loss_queryset = loss_queryset.prefetch_related('infrastructures')
        if is_expanded(self.request, 'loss'):
            queryset = queryset.prefetch_related(Prefetch(
                'loss', loss_queryset)
            )

        return queryset

    @action(detail=True, name='Incident Response')
    def response(self, request, pk=None, version=None):
        # TODO: dynmaic distance
        distance = self.request.query_params.get('distance', 10)  # km
        incident = self.get_object()
        resources = None

        location = incident.point or incident.polygon
        if location:
            resources = Resource.objects.filter(
                point__distance_lte=(
                    location, D(km=distance)
                ))\
                .annotate(
                    distance=Distance("point", location)
            ).select_related('polymorphic_ctype').order_by('distance')

        meta = self.request.query_params.get('meta')
        if meta:
            serializer = DetailResponseSerializer(resources, many=True)
        else:
            serializer = ResponseSerializer(resources, many=True)
        return Response(serializer.data)
