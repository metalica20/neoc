from rest_framework import viewsets
from .serializers import (
    FlowSerializer,
    ReleaseSerializer,
)
from .models import (
    Flow,
    Release,
)


class FlowViewSet(viewsets.ModelViewSet):
    serializer_class = FlowSerializer
    queryset = Flow.objects.all()


class ReleaseViewSet(viewsets.ModelViewSet):
    serializer_class = ReleaseSerializer
    queryset = Release.objects.all()
