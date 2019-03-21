from django.contrib import admin
from .models import (
    Loss,
    People,
    Family,
    Livestock,
    Infrastructure,
    InfrastructureType,
    LivestockType,
)


class PeopleInline(admin.TabularInline):
    model = People
    extra = 1


class FamilyInline(admin.TabularInline):
    model = Family
    extra = 1


class InfrastructureInline(admin.StackedInline):
    model = Infrastructure
    extra = 1


class LivestockInline(admin.TabularInline):
    model = Livestock
    extra = 1


@admin.register(Loss)
class LossAdmin(admin.ModelAdmin):
    search_fields = Loss.autocomplete_search_fields()
    exclude = ('detail',)
    inlines = (
        PeopleInline,
        FamilyInline,
        LivestockInline,
        InfrastructureInline
    )

    admin.site.register([InfrastructureType, LivestockType])
