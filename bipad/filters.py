import django_filters
from django.contrib.gis.geos import GEOSGeometry
from django.core.validators import EMPTY_VALUES


class GeometryFilter(django_filters.Filter):
    def filter(self, qs, value):
        if value in EMPTY_VALUES:
            return qs

        geometry = GEOSGeometry(value)
        return self.get_method(qs)(**{'%s__%s' % (self.field_name, self.lookup_expr): geometry})
