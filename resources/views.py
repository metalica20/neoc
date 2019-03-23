from rest_flex_fields import FlexFieldsModelViewSet
from .serializers import (
    ResourceSerializer,
    DetailResourceSerializer,
)
from .models import Resource
from .filters import ResourceFilter


class ResourceViewSet(FlexFieldsModelViewSet):
    search_fields = ('title',)
    filter_class = ResourceFilter

    def get_queryset(self):
        queryset = Resource.objects.select_related('polymorphic_ctype').all()
        meta = self.request.query_params.get('meta')
        if meta or self.action == 'retrieve':
            return queryset
        return queryset.non_polymorphic()

    def get_serializer_class(self):
        meta = self.request.query_params.get('meta')
        if meta or self.action == 'retrieve':
            return DetailResourceSerializer
        return ResourceSerializer
