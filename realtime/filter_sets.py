import django_filters
from .models import (
    Earthquake,
    River,
    Rain,
)


class RiverFilter(django_filters.FilterSet):
    water_level__gt = django_filters.IsoDateTimeFilter(
        field_name='water_level',
        lookup_expr='gte',
    )
    water_level__lt = django_filters.IsoDateTimeFilter(
        field_name='water_level',
        lookup_expr='lte',
    )

    class Meta:
        model = River
        fields = {
            'status': ['iexact'],
        }


class RainFilter(django_filters.FilterSet):
    class Meta:
        model = Rain
        fields = {
            'status': ['iexact'],
        }


class EarthquakeFilter(django_filters.FilterSet):
    event__on__gt = django_filters.IsoDateTimeFilter(
        field_name='event_on',
        lookup_expr='gte',
    )
    event__on__lt = django_filters.IsoDateTimeFilter(
        field_name='event_on',
        lookup_expr='lte',
    )
    magnitude__gt = django_filters.NumberFilter(
        field_name='magnitude',
        lookup_expr='gte',
    )
    magnitude__lt = django_filters.NumberFilter(
        field_name='magnitude',
        lookup_expr='lte',
    )

    class Meta:
        model = Earthquake
        fields = {
            'address': ['icontains'],
        }
