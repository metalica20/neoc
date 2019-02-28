from django.utils import timezone
from rest_framework import viewsets
from .filter_set import AlertFilter
from .serializers import AlertSerializer
from .models import Alert


class AlertViewSet(viewsets.ModelViewSet):
    serializer_class = AlertSerializer
    filter_class = AlertFilter
    search_fields = ('title',)
    queryset = Alert.objects.filter(verified=True).exclude(
        expire_on__lte=timezone.now()
    )
