import django_filters
from .models import (
    Document,
)


class DocumentFilter(django_filters.FilterSet):

    class Meta:
        model = Document
        fields = ('category', 'province', 'district', 'municipality')
