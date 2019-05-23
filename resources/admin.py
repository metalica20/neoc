from django.contrib.gis import (
    admin,
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
    Cultural,
)
from .permissions import get_queryset_for_user


@admin.register(Resource)
class ResourceAdmin(GeoPolymorphicParentModelAdmin):
    exclude = ('ward',)
    base_model = Resource
    child_models = (Education, Health, Finance, Tourism,
                    Communication, Governance, Industry, Cultural)
    list_filter = ('ward__municipality__district',)
    search_fields = Resource.autocomplete_search_fields()

    def get_queryset(self, request):
        queryset = super().get_queryset(request)
        queryset = get_queryset_for_user(queryset, request.user)
        return queryset


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


@admin.register(Cultural)
class CulturalAdmin(ResourceAdmin):
    base_model = Cultural
    show_in_index = True
