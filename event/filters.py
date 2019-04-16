import django_filters
from hazard.models import Hazard
from .models import Event


class EventFilter(django_filters.FilterSet):
    started_on__gt = django_filters.IsoDateTimeFilter(
        field_name='started_on',
        lookup_expr='gte',
    )
    started_on__lt = django_filters.IsoDateTimeFilter(
        field_name='started_on',
        lookup_expr='lte',
    )
    ended_on__gt = django_filters.IsoDateTimeFilter(
        field_name='ended_on',
        lookup_expr='gte',
    )
    ended_on__lt = django_filters.IsoDateTimeFilter(
        field_name='ended_on',
        lookup_expr='lte',
    )
    severity = django_filters.MultipleChoiceFilter(
        choices=Event.SEVERITY,
        lookup_expr='in',
    )

    class Meta:
        model = Event
        fields = []
