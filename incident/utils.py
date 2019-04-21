import datetime
from .models import Incident
from django.contrib.gis.measure import D
from loss.models import (
    People,
    Family,
    Livestock,
    Infrastructure
)


def get_similar_incident(incident):
    date_from = incident.incident_on + datetime.timedelta(-1)
    similar_incidents = Incident.objects.filter(
        incident_on__range=[date_from, incident.incident_on],
        hazard=incident.hazard
    ).exclude(id=incident.id)
    if incident.point:
        similar_incidents = similar_incidents.filter(
            point__distance_lte=(incident.point, D(km=5))
        )
    elif incident.polygon:
        similar_incidents = similar_incidents.filter(
            polygon__distance_lte=(incident.polygon, D(km=5))
        )
    else:
        return []
    return similar_incidents.order_by("-incident_on")


def get_followup_fields(incident_id):
    fields = []
    if People.objects.filter(loss__incident__id=incident_id, name__isnull=True).exists():
        fields.append('Peoples Name')
    if Family.objects.filter(loss__incident__id=incident_id, title__isnull=True).exists():
        fields.append('Family Name')
    if Livestock.objects.filter(
            loss__incident__id=incident_id,
            economic_loss__isnull=True
    ).exists():
        fields.append('Livestock Economic Loss')
    if Infrastructure.objects.filter(
            loss__incident__id=incident_id,
            economic_loss__isnull=True
    ).exists():
        fields.append('Infrastructure Economic Loss')

    return fields
