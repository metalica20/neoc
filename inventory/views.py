from django.utils import timezone
from rest_framework import viewsets
from .serializers import (
    CategorySerializer,
    ItemSerializer,
    InventorySerializer,
)
from .models import (
    Category,
    Item,
    Inventory,
)


class CategoryViewSet(viewsets.ModelViewSet):
    serializer_class = CategorySerializer
    search_fields = ('title',)
    queryset = Category.objects.all()


class ItemViewSet(viewsets.ModelViewSet):
    serializer_class = ItemSerializer
    search_fields = ('title',)
    filter_fields = ('category',)
    queryset = Item.objects.select_related('category').all()


class InventoryViewSet(viewsets.ModelViewSet):
    serializer_class = InventorySerializer
    search_fields = ('item',)
    filter_fields = ('item', 'resource')
    queryset = Inventory.objects.select_related(
        'item',
        'item__category'
    ).all()
