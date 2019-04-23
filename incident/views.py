import datetime
from rest_framework import status
from rest_framework.response import Response
from django.db.models import Prefetch
from rest_flex_fields import (
    FlexFieldsModelViewSet,
    is_expanded,
)
from .serializers import IncidentSerializer
from federal.models import Ward
from .models import Incident
from .filter_set import IncidentFilter
from loss.models import Loss
from django.core.cache import cache
from .tasks import update_lnd


class IncidentViewSet(FlexFieldsModelViewSet):
    serializer_class = IncidentSerializer
    filter_class = IncidentFilter
    search_fields = ('title', )
    permit_list_expands = [
        'event',
        'hazard',
        'wards',
        'wards.municipality',
        'loss',
        'loss.peoples',
        'loss.families',
        'loss.livestocks',
        'loss.infrastructures'
    ]

    def get_queryset(self):
        queryset = Incident.objects.filter(
            verified=True,
            approved=True,
        )
        loss_queryset = Loss.with_stat.all()
        if is_expanded(self.request, 'event'):
            queryset = queryset.select_related('event')
        if is_expanded(self.request, 'hazard'):
            queryset = queryset.select_related('hazard')
        if is_expanded(self.request, 'peoples'):
            loss_queryset = loss_queryset.prefetch_related('peoples')
        if is_expanded(self.request, 'wards'):
            queryset = queryset.prefetch_related(
                Prefetch('wards',
                         queryset=Ward.objects.defer(
                             'boundary',
                             'municipality__boundary'
                         ))
            )
        if is_expanded(self.request, 'families'):
            loss_queryset = loss_queryset.prefetch_related('families')
        if is_expanded(self.request, 'livestocks'):
            loss_queryset = loss_queryset.prefetch_related('livestocks')
        if is_expanded(self.request, 'infrastructures'):
            loss_queryset = loss_queryset.prefetch_related('infrastructures')
        if is_expanded(self.request, 'loss'):
            queryset = queryset.prefetch_related(Prefetch(
                'loss', loss_queryset)
            )

        return queryset

    def get_cached_response(self, request, *args, **kwargs):
        key = request.GET.urlencode()
        item = cache.get(key)
        if item is None:
            response = Response(status=status.HTTP_204_NO_CONTENT)
            # FIXME: async call
            update_lnd(
                super(IncidentViewSet, self).dispatch,
                request,
                *args,
                **kwargs
            )
        else:
            response, expiry = item
            response['Cache-Control'] = 'max-age=3600'
            if expiry < datetime.datetime.now():
                # FIXME: async call
                update_lnd(
                    super(IncidentViewSet, self).dispatch,
                    request,
                    *args,
                    **kwargs
                )
        return response

    def dispatch(self, request, *args, **kwargs):
        is_lnd = request.GET.get('lnd', 'false')
        if is_lnd.lower() == 'true':
            response = self.get_cached_response(request, *args, **kwargs)
        else:
            response = super().dispatch(request, *args, **kwargs)
        return response
