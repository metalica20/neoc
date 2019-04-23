from rest_flex_fields import (
    FlexFieldsModelViewSet,
    is_expanded,
)
from django.shortcuts import get_object_or_404
from rest_framework import generics
from django.contrib.gis.db.models.functions import Distance
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

    def filter_by_inventory_count(self, queryset, countDict):
        resource_ids = []
        for k, v in countDict.items():
            # TODO: tidy up
            item = k[:-6]
            query = """
                SELECT DISTINCT
                    resources_resource.id,
                    SUM ( inventory_inventory.quantity ) OVER (
                    PARTITION BY inventory_inventory.item_id,
                    inventory_inventory.item_id
                    ORDER BY
                        resources_resource.distance,
                        resources_resource.id
                        ) AS item_sum
                    FROM
                    ({}) AS resources_resource
                JOIN inventory_inventory ON inventory_inventory.resource_id = resources_resource.id
                    AND inventory_inventory.item_id = {}
            """.format(queryset.query, item)
            filtered_query = """
                SELECT * from
                ({}) as q
                where q.item_sum < {}
            """.format(query, v)
            limit = len(Resource.objects.raw(filtered_query))+1
            resources = Resource.objects.raw(query + " LIMIT {}".format(limit))
            resource_ids.extend([resource.id for resource in resources])
        return queryset.filter(pk__in=resource_ids)

    def get_queryset(self):
        incident_id = self.kwargs.get('pk')
        incident = get_object_or_404(Incident, pk=incident_id)
        queryset = Resource.objects.all()
        location = incident.point or incident.polygon
        if location:
            queryset = queryset.annotate(
                distance=Distance("point", location),
            )
        else:
            queryset = queryset.none()
        return queryset

    def filter_queryset(self, queryset):
        queryset = super().filter_queryset(queryset)
        countDict = {k: v for k, v in self.request.query_params.items() if k.endswith('_count')}
        if countDict:
            queryset = self.filter_by_inventory_count(queryset, countDict)
        else:
            distance__gte = self.request.query_params.get('distance__gte', 0)  # km
            distance__lte = self.request.query_params.get('distance__lte', 0)  # km
            queryset = queryset.filter(
                distance__lte=distance__lte*1000,
                distance__gte=distance__gte*1000,
            )
        return queryset.select_related('polymorphic_ctype').order_by('distance')

    def get_serializer_class(self):
        meta = self.request.query_params.get('meta')
        if meta:
            return DetailResponseSerializer
        return ResponseSerializer
