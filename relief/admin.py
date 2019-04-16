from django.contrib import admin
from .models import (
    Flow,
    Release,
    ReleaseStatus,
    FiscalYear,
)


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
        'provider_organization__title',
        'incident__title',
        'person__title',
    )
    list_display = (
        'provider_organization',
        'incident',
        'person',
        'status',
        'amount',
    )
    list_filter = ('status',)


admin.site.register([ReleaseStatus, FiscalYear])
