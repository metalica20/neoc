import django_filters
from django.contrib.contenttypes.models import ContentType
from rest_framework import (
    viewsets,
    filters,
)
from .serializers import ResourceSerializer
from .models import Resource
from federal.models import (
    Municipality,
    District,
    Province,
)


class ResourceFilter(django_filters.FilterSet):
    municipality = django_filters.ModelChoiceFilter(
        label="Municipality",
        field_name='ward__municipality',
        queryset=Municipality.objects.all()
    )
    district = django_filters.ModelChoiceFilter(
        label="District",
        field_name='ward__municipality__district',
        queryset=District.objects.all()
    )
    province = django_filters.ModelChoiceFilter(
        label="Province",
        field_name='ward__municipality__district__province',
        queryset=Province.objects.all()
    )
    resource_type = django_filters.ModelMultipleChoiceFilter(
        label="Resource Type",
        field_name='polymorphic_ctype__model',
        to_field_name='model',
        queryset=ContentType.objects.filter(
            app_label='resources').exclude(model='resource'),
    )

    class Meta:
        model = Resource
        fields = ('ward',)


class ResourceViewSet(viewsets.ModelViewSet):
    serializer_class = ResourceSerializer
    search_fields = ('title',)
    filter_backends = (django_filters.rest_framework.DjangoFilterBackend,
                       filters.SearchFilter, filters.OrderingFilter)
    filter_class = ResourceFilter
    queryset = Resource.objects.non_polymorphic().select_related('polymorphic_ctype').all()
