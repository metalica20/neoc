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
    def clean(self):
        name = self.cleaned_data.get("name")
        count = self.cleaned_data.get("count")
        if name and count != 1:
            raise ValidationError("When name is given, count must be 1")


class FamilyForm(forms.ModelForm):
    def clean(self):
        title = self.cleaned_data.get("title")
        count = self.cleaned_data.get("count")
        if title and count != 1:
            raise ValidationError("When title is given, count must be 1")


class PeopleInline(admin.TabularInline):
    model = People
    form = PeopleForm
    extra = 1


class FamilyInline(admin.TabularInline):
    model = Family
    form = FamilyForm
    extra = 1


class InfrastructureInline(admin.TabularInline):
    model = Infrastructure
    form = InfrastructureForm
    extra = 1


class LivestockInline(admin.TabularInline):
    model = Livestock
    form = LivestockForm
    extra = 1


class AgricultureInline(admin.TabularInline):
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


admin.site.register([Country, InfrastructureUnit])
