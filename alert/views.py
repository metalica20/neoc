from django.utils import timezone
from rest_flex_fields import FlexFieldsModelViewSet
from .filter_set import AlertFilter
from .serializers import AlertSerializer
from .models import Alert


class AlertViewSet(FlexFieldsModelViewSet):
    serializer_class = AlertSerializer
    filter_class = AlertFilter
    search_fields = ('title',)
    queryset = Alert.objects\
        .filter(verified=True, public=True, started_on__lte=timezone.now())\
        .exclude(expire_on__lte=timezone.now())
    permit_list_expands = ['event']
