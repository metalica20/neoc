from django.contrib import admin
from .models import (
    Loss,
    People,
    Family,
    Livestock,
    Infrastructure,
    InfrastructureType,
    LivestockType,
    Country,
    AgricultureType,
    Agriculture,
    InfrastructureUnit,
)
from django import forms
from django.core.exceptions import ValidationError
from mptt.admin import MPTTModelAdmin
from mptt.forms import TreeNodeChoiceField
from incident.utils import get_followup_fields
from federal.models import (
    District,
    Municipality,
    Ward
)
from django_select2.forms import ModelSelect2Widget
from django.utils.translation import ugettext_lazy as _
from jet.filters import RelatedFieldAjaxListFilter
from django.urls import reverse
from django.utils.html import format_html
from jet.filters import DateRangeFilter
from .permissions import (
    get_loss_queryset_for_user,
    get_losstype_queryset_for_user,
    get_infrastructure_queryset_for_user,
)


class AgricultureForm(forms.ModelForm):
    type = TreeNodeChoiceField(queryset=AgricultureType.objects.all())


class InfrastructureForm(forms.ModelForm):
    type = TreeNodeChoiceField(queryset=InfrastructureType.objects.all())


class LivestockForm(forms.ModelForm):
    type = TreeNodeChoiceField(queryset=LivestockType.objects.all())


@admin.register(AgricultureType)
class AgricultureTypeAdmin(MPTTModelAdmin):
    mptt_level_indent = 20


@admin.register(InfrastructureType)
class InfrastructureTypeAdmin(MPTTModelAdmin):
    mptt_level_indent = 20


@admin.register(LivestockType)
class LivestockTypeAdmin(MPTTModelAdmin):
    mptt_level_indent = 20


class PeopleForm(forms.ModelForm):
    def __init__(self, *args, **kwargs):
        instance = kwargs.get('instance', None)
        super(PeopleForm, self).__init__(*args, **kwargs)
        if instance:
            ward = People.objects.values('ward').filter(id=instance.id)
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
        label=_("District"),
        widget=ModelSelect2Widget(
            model=District,
            search_fields=['title__icontains'],
        )
    )
    municipality = forms.ModelChoiceField(
        queryset=Municipality.objects.all(),
        required=False,
        label=_("Municipality"),
        widget=ModelSelect2Widget(
            model=Municipality,
            search_fields=['title__icontains'],
            dependent_fields={'district': 'district'},
        )
    )
    ward = forms.ModelChoiceField(
        queryset=Ward.objects.all(),
        required=False,
        label=_("Ward"),
        widget=ModelSelect2Widget(
            model=Ward,
            search_fields=['title__icontains'],
            dependent_fields={'municipality': 'municipality'},
        )
    )

    def clean(self):
        name = self.cleaned_data.get("name")
        count = self.cleaned_data.get("count")
        if name and count != 1:
            raise ValidationError("When name is given, count must be 1")

    class Meta:
        model = People
        fields = (
            'status',
            'name',
            'age',
            'gender',
            'nationality',
            'district',
            'municipality',
            'ward',
            'below_poverty',
            'disability',
            'count',
        )


class FamilyForm(forms.ModelForm):
    district = forms.ModelChoiceField(
        queryset=District.objects.all(),
        required=False,
        label=_("District"),
        widget=ModelSelect2Widget(
            model=District,
            search_fields=['title__icontains'],
        )
    )
    municipality = forms.ModelChoiceField(
        queryset=Municipality.objects.all(),
        required=False,
        label=_("Municipality"),
        widget=ModelSelect2Widget(
            model=Municipality,
            search_fields=['title__icontains'],
            dependent_fields={'district': 'district'},
        )
    )
    ward = forms.ModelChoiceField(
        queryset=Ward.objects.all(),
        required=False,
        label=_("Ward"),
        widget=ModelSelect2Widget(
            model=Ward,
            search_fields=['title__icontains'],
            dependent_fields={'municipality': 'municipality'},
        )
    )

    def clean(self):
        title = self.cleaned_data.get("title")
        count = self.cleaned_data.get("count")
        if title and count != 1:
            raise ValidationError("When title is given, count must be 1")

    class Meta:
        model = Family
        fields = (
            'title',
            'status',
            'district',
            'municipality',
            'ward',
            'below_poverty',
            'phone_number',
            'count',
        )


class PeopleInline(admin.StackedInline):
    model = People
    form = PeopleForm
    extra = 1

    class Media:
        js = (
            'https://code.jquery.com/jquery-3.3.1.min.js',
        )


class FamilyInline(admin.StackedInline):
    model = Family
    form = FamilyForm
    extra = 1


class InfrastructureInline(admin.StackedInline):
    model = Infrastructure
    form = InfrastructureForm
    extra = 1


class LivestockInline(admin.StackedInline):
    model = Livestock
    form = LivestockForm
    extra = 1


class AgricultureInline(admin.StackedInline):
    model = Agriculture
    form = AgricultureForm
    extra = 1


@admin.register(Loss)
class LossAdmin(admin.ModelAdmin):
    search_fields = Loss.autocomplete_search_fields()
    exclude = ('detail',)
    inlines = (
        PeopleInline,
        FamilyInline,
        LivestockInline,
        InfrastructureInline,
        AgricultureInline,
    )

    def save_model(self, request, obj, form, change):
        super().save_model(request, obj, form, change)
        if hasattr(obj, 'incident'):
            fields = get_followup_fields(obj.incident.id)
            if len(fields):
                obj.incident.need_followup = True
                obj.incident.save()

    def get_queryset(self, request):
        queryset = super().get_queryset(request)
        queryset = get_loss_queryset_for_user(queryset, request.user)
        return queryset


class BaseLossAdmin(admin.ModelAdmin):
    search_fields = ['loss__incident__title']
    list_select_related = [
        'loss__incident'
    ]
    list_filter = (
        ('loss__incident', RelatedFieldAjaxListFilter),
        ('loss__incident__incident_on', DateRangeFilter),
    )
    list_display_links = 'incident',

    def has_add_permission(self, request):
        return False

    def incident(self, obj):
        if hasattr(obj.loss, 'incident'):
            return format_html('<a href="{}">{}</a>'.format(
                reverse('admin:incident_incident_change', args=[obj.loss.incident.id]),
                obj.loss.incident,
            ))

    def incident_on(self, obj):
        if hasattr(obj.loss, 'incident'):
            return obj.loss.incident.incident_on

    def get_queryset(self, request):
        queryset = super().get_queryset(request)
        queryset = get_losstype_queryset_for_user(queryset, request.user)
        return queryset


@admin.register(People)
class PeopleAdmin(BaseLossAdmin):
    search_fields = BaseLossAdmin.search_fields + ['name']
    list_display = ('incident', 'incident_on', 'name', 'status',
                    'age', 'gender', 'disability', 'count')
    list_select_related = (
        'loss__incident',
    )
    list_filter = (
        ('loss__incident', RelatedFieldAjaxListFilter),
    )

    def incident(self, obj):
        if hasattr(obj.loss, 'incident'):
            return obj.loss.incident


@admin.register(Family)
class FamilyAdmin(BaseLossAdmin):
    search_fields = ('title',)
    list_display = ('incident', 'incident_on', 'title', 'status', 'below_poverty', 'count')


@admin.register(Livestock)
class LivestockAdmin(BaseLossAdmin):
    search_fields = ('title',)
    list_display = ('incident', 'incident_on', 'title', 'type', 'status', 'count', 'economic_loss')
    list_select_related = (
        'loss__incident',
        'type',
    )


@admin.register(Infrastructure)
class InfrastructureAdmin(BaseLossAdmin):
    search_fields = ('title',)
    list_display = ('incident',  'incident_on', 'title', 'type', 'status', 'equipment_value',
                    'beneficiary_owner', 'economic_loss', 'count')

    def get_queryset(self, request):
        queryset = super().get_queryset(request)
        queryset = get_infrastructure_queryset_for_user(queryset, request.user)
        return queryset


@admin.register(Agriculture)
class AgricultureAdmin(BaseLossAdmin):
    search_fields = ('title',)
    list_display = ('incident', 'incident_on', 'type', 'beneficiary_owner', 'quantity')


admin.site.register([Country, InfrastructureUnit])
