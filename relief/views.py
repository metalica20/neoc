from rest_framework import viewsets
from .serializers import (
    FlowSerializer,
    ReleaseSerializer,
)
from .models import (
    Flow,
    Release,
)
from rest_framework.permissions import IsAuthenticated
from .filter_sets import ReleaseFilter


class FlowViewSet(viewsets.ModelViewSet):
    permission_classes = (IsAuthenticated,)
    serializer_class = FlowSerializer
    queryset = Flow.objects.all()


class ReleaseViewSet(viewsets.ModelViewSet):
    permission_classes = (IsAuthenticated,)
    serializer_class = ReleaseSerializer
    filter_class = ReleaseFilter
    queryset = Release.objects.all()
