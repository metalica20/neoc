from django.contrib import admin
from .models import (
    Flow,
    Release,
    ReleaseStatus,
    FiscalYear,
)
from django import forms
from federal.models import (
    District,
    Municipality,
    Ward
)
from django_select2.forms import ModelSelect2Widget


class ReleaseForm(forms.ModelForm):
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

    class Meta:
        Model = Release
        fields = [
            'provider_organization',
            'incident',
            'district',
            'municipality',
            'ward',
            'person',
            'beneficiary',
            'beneficiary_owner',
            'status',
            'amount',
            'description',
        ]


@admin.register(Flow)
class FlowAdmin(admin.ModelAdmin):
    search_fields = (
        'receiver_organization__title',
        'provider_organization__title',
        'event__title',
    )
    list_display = (
        'event',
        'receiver_organization',
        'provider_organization',
        'type',
        'amount',
        'fiscal_year',
        'date',
    )
    list_filter = ('type', 'fiscal_year', 'event')


@admin.register(Release)
class ReleaseAdmin(admin.ModelAdmin):
    search_fields = (
        'provider_organization__title',
        'incident__title',
        'person__title',
    )
    list_display = (
        'provider_organization',
        'incident',
        'person',
        'status',
        'amount',
    )
    list_filter = ('status',)

    form = ReleaseForm

    class Media:
        css = {
            'all': ('federal/css/django_select2.css',)
        }


admin.site.register([ReleaseStatus, FiscalYear])
