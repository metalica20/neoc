from django.db import models
from rest_framework import (
    viewsets,
)
from .serializers import HazardSerializer
from .models import Hazard


class HazardViewSet(viewsets.ModelViewSet):
    serializer_class = HazardSerializer
    search_fields = ('title',)
    queryset = Hazard.objects.all().annotate(
        incident_count=models.Count('incidents')
    ).order_by('-incident_count')
