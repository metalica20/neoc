from rest_framework import (
    viewsets,
)
from .serializers import EventSerializer
from .models import Event
from .filters import EventFilter


class EventViewSet(viewsets.ModelViewSet):
    serializer_class = EventSerializer
    search_fields = ('title',)
    filter_class = EventFilter
    queryset = Event.objects.all()
