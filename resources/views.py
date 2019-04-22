from rest_flex_fields import (
    FlexFieldsModelViewSet,
    is_expanded,
)
from django.shortcuts import get_object_or_404
from rest_framework import generics
from django.contrib.gis.db.models.functions import Distance
from django.contrib.gis.measure import D
from .serializers import (
    ResourceSerializer,
    DetailResourceSerializer,
    ResponseSerializer,
    DetailResponseSerializer,
)
from .models import Resource
from .filters import ResourceFilter
from incident.models import Incident


class ResourceViewSet(FlexFieldsModelViewSet):
    search_fields = ('title',)
    filter_class = ResourceFilter
    permit_list_expands = [
        'inventories',
    ]

    def get_queryset(self):
        queryset = Resource.objects.select_related('polymorphic_ctype').all()
        if is_expanded(self.request, 'inventories'):
            queryset = queryset.prefetch_related('inventories')
        meta = self.request.query_params.get('meta')
        if meta or self.action == 'retrieve':
            return queryset
        return queryset.non_polymorphic()

    def get_serializer_class(self):
        meta = self.request.query_params.get('meta')
        if meta or self.action == 'retrieve':
            return DetailResourceSerializer
        return ResourceSerializer


class ResponseList(generics.ListAPIView):
    search_fields = ('title',)
    filter_class = ResourceFilter
    permit_list_expands = [
        'inventories',
    ]

    def calculate_max_distance(self, queryset):
        countDict = {k: v for k, v in self.request.query_params.items() if k.endswith('count')}
        if countDict:
            # Logic here
            print(self.request.query_params)
            return 20
        return self.request.query_params.get('distance__lte', 10)  # km

    def get_queryset(self):
        incident_id = self.kwargs.get('pk')
        incident = get_object_or_404(Incident, pk=incident_id)
        queryset = Resource.objects.all()
        if is_expanded(self.request, 'inventories'):
            queryset = queryset.prefetch_related('inventories')
        location = incident.point or incident.polygon
        if location:
            queryset = queryset.annotate(
                distance=Distance("point", location)
            ).select_related('polymorphic_ctype').order_by('distance')
        else:
            queryset = queryset.none()
        return queryset

    def filter_queryset(self, queryset):
        queryset = super().filter_queryset(queryset)
        distance__gte = self.request.query_params.get('distance__gte', 0)  # km
        distance__lte = self.calculate_max_distance(queryset)
        queryset = queryset.filter(
            distance__lte=distance__lte*1000,
            distance__gte=distance__gte*1000,
        )
        return queryset

    def get_serializer_class(self):
        meta = self.request.query_params.get('meta')
        if meta:
            return DetailResponseSerializer
        return ResponseSerializer
