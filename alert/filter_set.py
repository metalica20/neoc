import django_filters
from hazard.models import Hazard
from .models import Alert


class AlertFilter(django_filters.FilterSet):
    started_on__gt = django_filters.IsoDateTimeFilter(
        field_name='started_on',
        lookup_expr='gte',
    )
    started_on__lt = django_filters.IsoDateTimeFilter(
        field_name='started_on',
        lookup_expr='lte',
    )
    created_on__gt = django_filters.IsoDateTimeFilter(
        field_name='created_on',
        lookup_expr='gte',
    )
    created_on__lt = django_filters.IsoDateTimeFilter(
        field_name='created_on',
        lookup_expr='lte',
    )
    hazard = django_filters.ModelMultipleChoiceFilter(
        queryset=Hazard.objects.all(),
        lookup_expr='in',
        widget=django_filters.widgets.CSVWidget,
    )

    class Meta:
        model = Alert
        fields = ['event', ]
