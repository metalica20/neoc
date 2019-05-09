import os
import geocoder
import datetime
from .models import Incident
from django.contrib.gis.measure import D
from loss.models import (
    People,
    Family,
    Livestock,
    Infrastructure
)
from django.contrib.gis.geos import GEOSGeometry, MultiPolygon


GOOGLE_MAP_API_KEY = os.environ.get('GOOGLE_MAPS_API_KEY')


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


def generate_polygon_from_wards(wards):
    polygon = GEOSGeometry(wards[0].boundary)
    if len(wards) > 1:
        for ward in wards[1:]:
            polygon = polygon.union(GEOSGeometry(ward.boundary))
        return MultiPolygon(polygon)
    return polygon


def get_incident_title(incident):
    location = geocoder.google(
        [incident.point.y, incident.point.x],
        components="country:NP",
        method='reverse',
        key=GOOGLE_MAP_API_KEY
    )
    if location.city:
        return "%s at %s" % (incident.hazard.title_en, location.city)
    else:
        return "%s" % incident.hazard
