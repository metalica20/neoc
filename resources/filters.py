import django_filters
from django.contrib.contenttypes.models import ContentType
from federal.models import (
    Ward,
    Municipality,
    District,
    Province,
)
from .models import Resource


class ResourceFilter(django_filters.FilterSet):
    ward = django_filters.ModelMultipleChoiceFilter(
        label="Ward is in",
        field_name='ward',
        lookup_expr='in',
        queryset=Ward.objects.all(),
        widget=django_filters.widgets.CSVWidget,
    )
    municipality = django_filters.ModelMultipleChoiceFilter(
        label="Municipality is in",
        field_name='ward__municipality',
        lookup_expr='in',
        queryset=Municipality.objects.all(),
        widget=django_filters.widgets.CSVWidget,
    )
    district = django_filters.ModelMultipleChoiceFilter(
        label="District is in",
        field_name='ward__municipality__district',
        lookup_expr='in',
        queryset=District.objects.all(),
        widget=django_filters.widgets.CSVWidget,
    )
    province = django_filters.ModelMultipleChoiceFilter(
        label="Province is in",
        field_name='ward__municipality__district__province',
        lookup_expr='in',
        queryset=Province.objects.all(),
        widget=django_filters.widgets.CSVWidget,
    )
    resource_type = django_filters.ModelMultipleChoiceFilter(
        label="Resource Type is in",
        field_name='polymorphic_ctype__model',
        to_field_name='model',
        lookup_expr='in',
        queryset=ContentType.objects.filter(
            app_label='resources').exclude(model='resource'),
    )

    class Meta:
        model = Resource
        fields = []
