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
from loss.models import People


class ReleaseForm(forms.ModelForm):

    def __init__(self, *args, **kwargs):
        instance = kwargs.get('instance', None)
        super(ReleaseForm, self).__init__(*args, **kwargs)
        self.fields['person'].widget.queryset = People.objects.filter(name__isnull=False)
        self.fields['beneficiary'].queryset = People.objects.filter(name__isnull=False)
        if instance:
            ward = Release.objects.values('ward').filter(id=instance.id)
            if ward[0]['ward']:
                municipality = Ward.objects.values(
                    'municipality',
                    'municipality__district'
                ).filter(id=ward[0]['ward'])
                self.fields['municipality'].initial = municipality[0]['municipality']
                self.fields['district'].initial = municipality[0]['municipality__district']

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
    person = forms.ModelChoiceField(
        queryset=People.objects.filter(name__isnull=False),
        required=False,
        widget=ModelSelect2Widget(
            model=People,
            search_fields=['name__icontains'],
            dependent_fields={
                'ward': 'ward',
                'municipality': 'ward__municipality',
                'district': 'ward__municipality__district'
            },
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
            'beneficiary_other',
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
        'incident__title',
        'person__name',
        'provider_organization__title',
        'ward__municipality__title',
    )
    list_display = (
        'provider_organization',
        'incident',
        'person',
        'ward',
        'status',
        'amount',
    )
    list_filter = ('status',)

    form = ReleaseForm

    class Media:
        js = (
            'https://code.jquery.com/jquery-3.3.1.min.js',
        )


admin.site.register([ReleaseStatus, FiscalYear])
