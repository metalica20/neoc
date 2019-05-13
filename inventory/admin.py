from django.contrib import admin
from .models import (
    Inventory,
    Item,
    Category,
)
from django import forms
from federal.models import (
    District,
    Municipality,
    Ward
)
from django_select2.forms import ModelSelect2Widget
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
class InventoryAdmin(admin.ModelAdmin):
    list_display = ['item', 'resource', 'quantity']
    form = InventoryForm


@admin.register(Item)
class ItemAdmin(admin.ModelAdmin):

    def get_readonly_fields(self, request, obj=None):
        if obj:
            return ["unit"]
        else:
            return []


admin.site.register(Category)
