from django.contrib.auth import get_permission_codename
from django.contrib import admin
from bipad.admin import GeoModelAdmin
from .models import Incident


@admin.register(Incident)
class IncidentAdmin(GeoModelAdmin):
    search_fields = ('title', 'description', 'street_address', 'hazard__title')
    list_display = ('title', 'hazard', 'source', 'verified', 'incident_on')
    list_filter = ('hazard', 'source', 'verified', 'inducer')
    autocomplete_fields = ('wards',)
    exclude = ('detail',)
    actions = ("verify",)

    def verify(self, request, queryset):
        queryset.update(verified=True)
    verify.allowed_permissions = ('can_verify',)
    verify.short_description = 'Mark incidents as verified'

    def has_can_verify_permission(self, request):
        opts = self.opts
        codename = get_permission_codename('can_verify', opts)
        return request.user.has_perm('%s.%s' % (opts.app_label, codename))

    def get_form(self, request, obj=None, **kwargs):
        form = super().get_form(request, obj, **kwargs)
        form.base_fields['loss'].disabled = True
        if request.user.groups.filter(name='Nepal Police').exists():
            form.base_fields['source'].initial = 'nepal_police'
            form.base_fields['source'].disabled = True
        if not self.has_can_verify_permission(request):
            form.base_fields['verified'].disabled = True
        return form

    def get_queryset(self, request):
        queryset = super().get_queryset(request)
        if request.user.groups.filter(name='Nepal Police').exists():
            return queryset.filter(source__name='nepal_police')
        return queryset
