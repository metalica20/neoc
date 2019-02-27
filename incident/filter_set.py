import django_filters
from hazard.models import Hazard
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
    hazard = django_filters.ModelMultipleChoiceFilter(
        queryset=Hazard.objects.all(),
        lookup_expr='in',
        widget=django_filters.widgets.CSVWidget,
    )

    class Meta:
        model = Incident
        fields = ['event', ]
