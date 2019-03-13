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


class InfrastructureInline(admin.TabularInline):
    model = Infrastructure
    extra = 1


class LivestockInline(admin.TabularInline):
    model = Livestock
    extra = 1


@admin.register(Loss)
class LossAdmin(admin.ModelAdmin):
    exclude = ('detail',)
    inlines = (PeopleInline, FamilyInline,
               LivestockInline, InfrastructureInline)

    def get_model_perms(self, request):
        return {}


admin.site.register([InfrastructureType, LivestockType])
