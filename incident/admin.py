from django.contrib.auth import get_permission_codename
from django.contrib import admin
from bipad.admin import GeoModelAdmin
from .models import (
    Incident,
    Document,
)
from federal.models import (
    Province,
    District,
    Municipality,
    Ward,
)
from django import forms
from django_select2.forms import (
    ModelSelect2Widget,
    ModelSelect2MultipleWidget,
)


class DocumentInline(admin.TabularInline):
    model = Document
    extra = 1


class AddressForm(forms.ModelForm):
    def __init__(self, *args, **kwargs):
        instance = kwargs.get('instance', None)
        super(AddressForm, self).__init__(*args, **kwargs)
        if instance:
            wards = Incident.objects.values('wards').filter(id=instance.id)
            if wards[0]['wards']:
                municipality = Ward.objects.values(
                    'municipality', 'municipality__district').filter(id=wards[0]['wards'])
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

    wards = forms.ModelMultipleChoiceField(
        queryset=Ward.objects.all(),
        required=False,
        widget=ModelSelect2MultipleWidget(
            model=Ward,
            search_fields=['title__icontains'],
            dependent_fields={'municipality': 'municipality'},
        )
    )

    class Meta:
        model = Incident
        fields = (
            'title',
            'cause',
            'source',
            'verified',
            'approved',
            'inducer',
            'point',
            'polygon',
            'incident_on',
            'reported_on',
            'event',
            'hazard',
            'loss',
            'district',
            'municipality',
            'wards',
            'street_address',
            'description'
        )


@admin.register(Incident)
class IncidentAdmin(GeoModelAdmin):
    search_fields = ('title', 'description', 'street_address', 'hazard__title')
    list_display = ('title', 'hazard', 'source', 'verified', 'incident_on')
    list_filter = ('hazard', 'source', 'verified', 'inducer')
    exclude = ('detail',)
    actions = ("verify", 'approve')
    inlines = (DocumentInline,)

    form = AddressForm

    class Media:
        css = {
            'all': ('federal/css/django_select2.css',)
        }

    def verify(self, request, queryset):
        queryset.update(verified=True)
    verify.allowed_permissions = ('can_verify',)
    verify.short_description = 'Mark incidents as verified'

    def approve(self, request, queryset):
        queryset.update(approved=True)
    approve.allowed_permissions = ('can_approve',)
    approve.short_description = 'Mark incidents as approved'

    def has_can_verify_permission(self, request):
        opts = self.opts
        codename = get_permission_codename('can_verify', opts)
        return request.user.has_perm('%s.%s' % (opts.app_label, codename))

    def has_can_approve_permission(self, request):
        opts = self.opts
        codename = get_permission_codename('can_approve', opts)
        return request.user.has_perm('%s.%s' % (opts.app_label, codename))

    def get_form(self, request, obj=None, **kwargs):
        form = super().get_form(request, obj, **kwargs)
        form.base_fields['loss'].disabled = True
        if request.user.groups.filter(name='Nepal Police').exists():
            form.base_fields['source'].initial = 'nepal_police'
            form.base_fields['source'].disabled = True
        if not self.has_can_verify_permission(request):
            form.base_fields['verified'].disabled = True
        if not self.has_can_approve_permission(request):
            form.base_fields['approved'].disabled = True
        return form

    def get_queryset(self, request):
        queryset = super().get_queryset(request)
        if request.user.groups.filter(name='Nepal Police').exists():
            return queryset.filter(source__name='nepal_police')
        return queryset


admin.site.register(Document)
