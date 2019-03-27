import django_filters
from bipad.filters import GeometryFilter
from federal.models import Ward


class WardFilter(django_filters.FilterSet):
    boundary__contains = GeometryFilter(field_name='boundary', lookup_expr='contains')

    class Meta:
        model = Ward
        fields = (
            'municipality',
            'municipality__district',
            'municipality__district__province',
        )
