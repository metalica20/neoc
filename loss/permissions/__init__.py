from incident.models import Incident
from incident.permissions import get_queryset_for_user as get_incident_queryset


def get_loss_queryset_for_user(queryset, user):
    incidents = get_incident_queryset(Incident.objects.all(), user)
    queryset = queryset.filter(incident__in=incidents).distinct()
    return queryset


def get_losstype_queryset_for_user(queryset, user):
    incidents = get_incident_queryset(Incident.objects.all(), user)
    queryset = queryset.filter(loss__incident__in=incidents).distinct()
    return queryset


def get_infrastructure_queryset_for_user(queryset, user):
    if user.is_superuser:
        incidents = get_incident_queryset(
            Incident.objects.all(), user
        )
    else:
        incidents = get_incident_queryset(
            Incident.objects.filter(loss__infrastructures__type__owner_organizations=user.profile.organization), user
        )
    queryset = queryset.filter(loss__incident__in=incidents).distinct()
    return queryset
