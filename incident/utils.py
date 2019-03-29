import datetime
from .models import Incident
from django.contrib.gis.measure import D


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
            polyon__distance_lte=(incident.polygon, D(km=5))
        )
    else:
        return []
    return similar_incidents.order_by("-incident_on")
