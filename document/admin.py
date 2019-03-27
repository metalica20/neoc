from reversion.admin import VersionAdmin
from django.contrib import admin
from .models import (
    Category,
    Document,
)
from federal.models import (
    Province,
    District,
    Municipality,
)
from django import forms
from django_select2.forms import ModelSelect2Widget
from bipad.admin import GeoModelAdmin


class AddressForm(forms.ModelForm):
    province = forms.ModelChoiceField(
        queryset=Province.objects.all(),
        required=False,
        widget=ModelSelect2Widget(
            model=Province,
            search_fields=['title__icontains'],
        )
    )
    district = forms.ModelChoiceField(
        queryset=District.objects.all(),
        required=False,
        widget=ModelSelect2Widget(
            model=District,
            search_fields=['title__icontains'],
            dependent_fields={'province': 'province'},
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

    class Meta:
        model = Document
        fields = '__all__'


@admin.register(Document)
class DocumentAdmin(VersionAdmin, GeoModelAdmin):
    form = AddressForm

    class Media:
        css = {
            'all': ('federal/css/django_select2.css',)
        }


admin.site.register(Category)
