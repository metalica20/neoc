from rest_framework import viewsets
from .filter_sets import (
    DocumentFilter,
)
from .serializers import (
    DocumentSerializer
)
from .models import (
    Document,
)


class DocumentViewSet(viewsets.ModelViewSet):
    serializer_class = DocumentSerializer
    filter_class = DocumentFilter
    search_fields = ('title', 'event')
    queryset = Document.objects.all()
