from django.contrib import admin
from .models import (
    Organization,
    Project,
)
from django import forms
from federal.models import (
    District,
    Municipality,
    Ward
)
from django_select2.forms import (
    ModelSelect2Widget,
    ModelSelect2MultipleWidget
)


class OrganizationForm(forms.ModelForm):
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
        model = Organization
        fields = [
            "title",
            "short_name",
            "long_name",
            "district",
            "municipality",
            "wards",
            "description"
        ]


class ProjectForm(forms.ModelForm):
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
        model = Project
        fields = [
            "title",
            "organization",
            "district",
            "municipality",
            "wards",
            "description"
        ]


@admin.register(Organization)
class OrganizationAdmin(admin.ModelAdmin):
    form = OrganizationForm

    class Media:
        css = {
            'all': ('federal/css/django_select2.css',)
        }


@admin.register(Project)
class ProjectAdmin(admin.ModelAdmin):
    form = ProjectForm

    class Media:
        css = {
            'all': ('federal/css/django_select2.css',)
        }