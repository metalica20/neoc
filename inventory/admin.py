from django.contrib import admin
from django import forms
from django_select2.forms import ModelSelect2Widget
from django.utils.html import format_html
from django.urls import reverse
from reversion.admin import VersionAdmin

from .permissions import get_queryset_for_user
from .models import (
    Inventory,
    Item,
    Category,
)
from federal.models import (
    District,
    Municipality,
    Ward
)
from resources.models import Resource


class InventoryForm(forms.ModelForm):
    def __init__(self, *args, **kwargs):
        instance = kwargs.get('instance', None)
        super(InventoryForm, self).__init__(*args, **kwargs)
        self.fields['resource'].autocomplete = False
        if instance:
            ward = Resource.objects.values('ward').filter(inventories__id=instance.id)
            if ward[0]['ward']:
                municipality = Ward.objects.values(
                    'municipality', 'municipality__district').filter(id=ward[0]['ward'])
                self.fields['municipality'].initial = municipality[0]['municipality']
                self.fields['district'].initial = municipality[0]['municipality__district']
                self.fields['ward'].initial = ward[0]['ward']

    district = forms.ModelChoiceField(
        queryset=District.objects.all(),
        required=False,
        widget=ModelSelect2Widget(
            model=District,
            search_fields=['title__icontains'],
        )
    )
    municipality = forms.ModelChoiceField(
        queryset=Municipality.objects.all(),
        required=False,
        widget=ModelSelect2Widget(
            model=Municipality,
            search_fields=['title__icontains'],
            dependent_fields={'district': 'district'},
        )
    )
    ward = forms.ModelChoiceField(
        queryset=Ward.objects.all(),
        required=False,
        widget=ModelSelect2Widget(
            model=Ward,
            search_fields=['title__icontains'],
            dependent_fields={'municipality': 'municipality'},
        )
    )
    resource = forms.ModelChoiceField(
        queryset=Resource.objects.all(),
        widget=ModelSelect2Widget(
            model=Resource,
            search_fields=['title__icontains'],
            dependent_fields={
                'ward': 'ward',
                'municipality': 'ward__municipality',
                'district': 'ward__municipality__district',
            },
        )
    )

    class Meta:
        model = Inventory
        fields = [
            'item',
            'district',
            'municipality',
            'ward',
            'resource',
            'quantity',
        ]


@admin.register(Inventory)
class InventoryAdmin(VersionAdmin):
    search_fields = ('item__category__title', 'item__title',)
    list_display = ('resource_link', 'item', 'quantity')
    list_filter = ('item__category',)
    list_display_links = 'resource_link',
    form = InventoryForm

    def resource_link(self, obj):
        return format_html('<a href="{}#/tab/inline_0/">{}</a>'.format(
            reverse('admin:resources_resource_change', args=[obj.resource.id]),
            obj.resource,
        ))
    resource_link.short_description = 'Resource'

    def get_queryset(self, request):
        queryset = super().get_queryset(request)
        return get_queryset_for_user(queryset, request.user)


@admin.register(Item)
class ItemAdmin(admin.ModelAdmin):

    def get_readonly_fields(self, request, obj=None):
        if obj:
            return ["unit"]
        else:
            return []


admin.site.register(Category)
