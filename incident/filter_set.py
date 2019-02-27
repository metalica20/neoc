import django_filters
from .models import Incident


class IncidentFilter(django_filters.FilterSet):
    incident_on__gt = django_filters.DateTimeFilter(
        field_name='incident_on',
        lookup_expr='gte',
    )
    incident_on__lt = django_filters.DateTimeFilter(
        field_name='incident_on',
        lookup_expr='lte',
    )

    class Meta:
        model = Incident
        fields = ['event', 'hazard']
