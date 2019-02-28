from rest_framework.decorators import action
from rest_framework.response import Response
from rest_framework import viewsets
from .serializers import IncidentSerializer
from resources.models import Resource
from resources.serializers import ResponseSerializer
from .models import Incident
from .filter_set import IncidentFilter

from django.contrib.gis.db.models.functions import Distance
from django.contrib.gis.measure import D


class IncidentViewSet(viewsets.ModelViewSet):
    serializer_class = IncidentSerializer
    filter_class = IncidentFilter
    search_fields = ('title', )
    queryset = Incident.objects.filter(verified=True)

    @action(detail=True, name='Incident Response')
    def response(self, request, pk=None, version=None):
        # TODO: dynmaic distance
        distance = self.request.query_params.get('distance', 200)  # km
        incident = self.get_object()
        resources = None

        if incident.point:
            resources = Resource.objects.filter(
                point__distance_lte=(
                    incident.point, D(km=distance)
                ))\
                .annotate(
                    distance=Distance("point", incident.point)
            ).order_by('distance')

        serializer = ResponseSerializer(resources, many=True)
        return Response(serializer.data)
