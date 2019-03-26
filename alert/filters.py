import django_filters
from hazard.models import Hazard
from .models import Alert
from federal.models import (
    District,
    Municipality,
    Province,
    Ward,
)


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
    ward = django_filters.ModelMultipleChoiceFilter(
        queryset=Ward.objects.all(),
        label='Ward is in',
        field_name='wards',
        lookup_expr='in',
        widget=django_filters.widgets.CSVWidget,
    )
    municipality = django_filters.ModelMultipleChoiceFilter(
        queryset=Municipality.objects.all(),
        label='Municipality is in',
        field_name='wards__municipality',
        lookup_expr='in',
        widget=django_filters.widgets.CSVWidget,
    )
    district = django_filters.ModelMultipleChoiceFilter(
        queryset=District.objects.all(),
        label='District is in',
        field_name='wards__municipality__district',
        lookup_expr='in',
        widget=django_filters.widgets.CSVWidget,
    )
    province = django_filters.ModelMultipleChoiceFilter(
        queryset=Province.objects.all(),
        label='Province is in',
        field_name='wards__municipality__district__province',
        lookup_expr='in',
        widget=django_filters.widgets.CSVWidget,
    )

    class Meta:
        model = Alert
        fields = ['event', ]
