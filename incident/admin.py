import json
from django.contrib.auth import get_permission_codename
from django.contrib import (
    admin,
    messages,
)
from django.utils.safestring import mark_safe
from django.http import HttpResponseRedirect
from django.utils.translation import ugettext_lazy as _
from django.contrib.gis.geos import GEOSGeometry
from misc.validators import validate_geojson
from django.core.exceptions import ValidationError
from django.utils.html import format_html
from django.urls import reverse
from jet.filters import DateRangeFilter
from reversion.admin import VersionAdmin

from bipad.admin import GeoModelAdmin
from .models import (
    Incident,
    Document,
)
from federal.models import (
    District,
    Municipality,
    Ward,
)
from django import forms
from django_select2.forms import (
    ModelSelect2Widget,
    ModelSelect2MultipleWidget,
)
from .utils import (
    get_similar_incident,
    get_followup_fields,
    get_incident_title,
    generate_polygon_from_wards,
)
from loss.notifications import send_user_notification
from .permissions import get_queryset_for_user


INCIDENT_FIELDS = (
    'hazard',
    'cause',
    'source',
    'district',
    'municipality',
    'wards',
    'street_address',
    'point',
    'geojson',
    'incident_on',
    'reported_on',
    'event',
    'loss',
    'description',
    'approved',
    'verified',
    'verification_message',
)


class DocumentInline(admin.TabularInline):
    model = Document
    extra = 1


class IncidentForm(forms.ModelForm):
    def __init__(self, *args, **kwargs):
        instance = kwargs.get('instance', None)
        super(IncidentForm, self).__init__(*args, **kwargs)
        if hasattr(self.fields, 'verification_message'):
            self.fields['verification_message'].widget.attrs['rows'] = 3
            self.fields['verification_message'].widget.attrs['columns'] = 15
        if instance:
            wards = Incident.objects.values('wards').filter(id=instance.id)
            if wards[0]['wards']:
                municipality = Ward.objects.values(
                    'municipality',
                    'municipality__district'
                ).filter(id=wards[0]['wards'])
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

    wards = forms.ModelMultipleChoiceField(
        queryset=Ward.objects.all(),
        required=False,
        label=_("Wards"),
        widget=ModelSelect2MultipleWidget(
            model=Ward,
            search_fields=['title__icontains'],
            dependent_fields={'municipality': 'municipality'},
        )
    )

    geojson = forms.FileField(
        required=False,
        validators=[validate_geojson],
        label=_('Geojson')
    )

    class Meta:
        model = Incident
        fields = INCIDENT_FIELDS

    def clean(self):
        if not(
                self.cleaned_data.get("wards") or
                self.cleaned_data.get("point") or
                self.cleaned_data.get("polygon") or
                self.cleaned_data.get("geojson")
        ):
            raise ValidationError(_("You need to add either wards or point or polygon or Geojson"))
        if not self.cleaned_data.get('verified'):
            if self.cleaned_data.get('verification_message'):
                raise ValidationError(_("You cannot write verification message if not verified"))


@admin.register(Incident)
class IncidentAdmin(VersionAdmin, GeoModelAdmin):
    search_fields = ('title', 'description', 'street_address', 'hazard__title')
    list_display = ('title', 'hazard', 'source', 'verified', 'incident_on', 'incident_actions')
    list_filter = (
        ('loss__incident__incident_on', DateRangeFilter),
        'need_followup',
        'hazard',
        'source',
        'verified',
        'approved',
    )
    exclude = ('detail', 'title')
    actions = ("verify", 'approve', "create_event")
    inlines = (DocumentInline,)

    form = IncidentForm

    def incident_actions(self, obj):
        return format_html(
            """
            <button>
                <a href="{}?incident={}">
                    Add Relief
                </a>
            </button>
            """.format(reverse('admin:relief_release_add'), obj.id)
        )

    def save_model(self, request, obj, form, change):
        if change:
            obj.updated_by = request.user
        else:
            obj.created_by = request.user

        geojson = form.cleaned_data.get('geojson')
        wards = form.cleaned_data.get('wards')

        # geojson takes precedence over others
        if geojson:
            geojson = json.loads(geojson.read().decode('utf-8'))
            obj.polygon = GEOSGeometry(json.dumps(geojson['geometry']))

        if obj.point and not wards:
            # point overwrites wards
            wards = Ward.objects.filter(boundary__contains=obj.point)
            form.cleaned_data['wards'] = wards

        if not obj.point and not wards:
            wards = Ward.objects.filter(boundary__contains=obj.polygon)
            form.cleaned_data['wards'] = wards

        if wards and not obj.polygon and not obj.point:
            polygon = generate_polygon_from_wards(wards)
            obj.point = GEOSGeometry(polygon).centroid

            # generate centroid from polygon
        if not obj.point and obj.polygon:
            obj.point = GEOSGeometry(obj.polygon).centroid

        obj.title = get_incident_title(obj)

        super().save_model(request, obj, form, change)
        followup_fields = get_followup_fields(obj.id)
        if len(followup_fields) or (obj.verified and obj.verification_message):
            obj.need_followup = True
            obj.save()

        similar_incidents = get_similar_incident(obj)
        for incident in similar_incidents:
            messages.add_message(request, messages.INFO, mark_safe(
                "Similar data <a href='%s'>%s</a> already exists"
                % (reverse('admin:incident_incident_change', args=[incident.id]), incident.title)
            ))

        send_user_notification(obj, change)

    def verify(self, request, queryset):
        queryset.update(verified=True)

    verify.allowed_permissions = ('verify',)
    verify.short_description = _('Mark incidents as verified')

    def approve(self, request, queryset):
        queryset.update(approved=True)

    approve.allowed_permissions = ('approve',)
    approve.short_description = _('Mark incidents as approved')

    def has_verify_permission(self, request):
        opts = self.opts
        codename = get_permission_codename('verify', opts)
        return request.user.has_perm('%s.%s' % (opts.app_label, codename))

    def has_approve_permission(self, request):
        opts = self.opts
        codename = get_permission_codename('approve', opts)
        return request.user.has_perm('%s.%s' % (opts.app_label, codename))

    def has_edit_permission(self, request):
        opts = self.opts
        codename = get_permission_codename('edit', opts)
        return request.user.has_perm('%s.%s' % (opts.app_label, codename))

    def changeform_view(self, request, object_id=None, form_url='', extra_context=None):
        if not self.has_edit_permission(request):
            extra_context = extra_context or {}
            extra_context['read_only'] = True
        return super().changeform_view(request, object_id, extra_context=extra_context)

    def get_form(self, request, obj=None, **kwargs):
        self.readonly_fields = []
        if not self.has_verify_permission(request):
            self.readonly_fields.append('verified')
            self.readonly_fields.append('verification_message')
        if not self.has_approve_permission(request):
            self.readonly_fields.append('approved')
        form = super().get_form(request, obj, **kwargs)
        if request.user.profile.organization == 'Nepal Police':
            form.base_fields['source'].initial = 'nepal_police'
            form.base_fields['source'].disabled = True
        return form

    def get_queryset(self, request):
        queryset = super().get_queryset(request)
        queryset = get_queryset_for_user(queryset, request.user)
        return queryset

    def create_event(self, request, queryset):
        incident_ids = ",".join(str(incident.id) for incident in queryset)
        return HttpResponseRedirect('/admin/event/event/add/?incident=%s' % incident_ids)

    create_event.short_description = _('Create Event')

    def change_view(self, request, object_id, form_url=''):
        followup_fields = get_followup_fields(object_id)
        if followup_fields:
            messages.add_message(
                request, messages.INFO,
                'Incident is incomplete. %s need followup' % ', '.join(followup_fields)
            )
        return super().change_view(
            request, object_id, form_url
        )


admin.site.register(Document)
