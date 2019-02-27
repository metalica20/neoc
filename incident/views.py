from .filter_set import IncidentFilter
from rest_framework import (
    viewsets,
)
from .serializers import IncidentSerializer
from .models import Incident


class IncidentViewSet(viewsets.ModelViewSet):
    serializer_class = IncidentSerializer
    filter_class = IncidentFilter
    search_fields = ('title',)
    queryset = Incident.objects.filter(verified=True)
