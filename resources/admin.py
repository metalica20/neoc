from django.contrib.gis import(
    admin,
    forms,
)
from bipad.admin import GeoPolymorphicParentModelAdmin
from .models import (
    Resource,
    Education,
    Health,
    Finance,
    Tourism,
    Communication,
    Governance,
    Industry,
)
from federal.models import (
    District,
    Municipality,
    Ward
)
from django_select2.forms import ModelSelect2Widget


class AddressForm(forms.ModelForm):
    def __init__(self, *args, **kwargs):
        instance = kwargs.get('instance', None)
        super(AddressForm, self).__init__(*args, **kwargs)
        if instance:
            ward = Resource.objects.values('ward').filter(id=instance.id)
            if ward[0]['ward']:
                municipality = Ward.objects.values('municipality','municipality__district').filter(id=ward[0]['ward'])
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

    class Meta:
        model = Resource
        fields = '__all__'


@admin.register(Resource)
class ResourceAdmin(GeoPolymorphicParentModelAdmin):
    form = AddressForm
    base_model = Resource
    child_models = (Education, Health, Finance, Tourism,
                    Communication, Governance, Industry)

    class Media:
        css = {
            'all': ('federal/css/django_select2.css',)
        }


@admin.register(Education)
class EducationAdmin(ResourceAdmin):
    base_model = Education
    show_in_index = True


@admin.register(Health)
class HealthAdmin(ResourceAdmin):
    base_model = Health
    show_in_index = True


@admin.register(Finance)
class FinanceAdmin(ResourceAdmin):
    base_model = Finance
    show_in_index = True


@admin.register(Tourism)
class TourismAdmin(ResourceAdmin):
    base_model = Tourism
    show_in_index = True


@admin.register(Communication)
class CommunicationAdmin(ResourceAdmin):
    base_model = Communication
    show_in_index = True


@admin.register(Governance)
class GovernanceAdmin(ResourceAdmin):
    base_model = Governance
    show_in_index = True


@admin.register(Industry)
class IndustryAdmin(ResourceAdmin):
    base_model = Industry
    show_in_index = True
