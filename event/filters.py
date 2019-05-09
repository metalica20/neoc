import django_filters
from hazard.models import Hazard
from .models import Event
from federal.models import (
    Province,
    District,
    Municipality,
    Ward
)


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
    hazard = django_filters.ModelMultipleChoiceFilter(
        queryset=Hazard.objects.all(),
        lookup_expr='in',
        widget=django_filters.widgets.CSVWidget,
    )
    ward = django_filters.ModelMultipleChoiceFilter(
        queryset=Ward.objects.all(),
        label='Ward is in',
        field_name='incidents__wards',
        lookup_expr='in',
        widget=django_filters.widgets.CSVWidget,
    )
    municipality = django_filters.ModelMultipleChoiceFilter(
        queryset=Municipality.objects.all(),
        label='Municipality is in',
        field_name='incidents__wards__municipality',
        lookup_expr='in',
        widget=django_filters.widgets.CSVWidget,
    )
    district = django_filters.ModelMultipleChoiceFilter(
        queryset=District.objects.all(),
        label='District is in',
        field_name='incidents__wards__municipality__district',
        lookup_expr='in',
        widget=django_filters.widgets.CSVWidget,
    )
    province = django_filters.ModelMultipleChoiceFilter(
        queryset=Province.objects.all(),
        label='Province is in',
        field_name='incidents__wards__municipality__district__province',
        lookup_expr='in',
        widget=django_filters.widgets.CSVWidget,
    )

    class Meta:
        model = Event
        fields = []
