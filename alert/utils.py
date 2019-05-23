import os
import geocoder
from .models import Alert
from django.contrib.gis.measure import D
from django.contrib.gis.geos import GEOSGeometry, MultiPolygon

GOOGLE_MAP_API_KEY = os.environ.get('GOOGLE_MAPS_API_KEY')


def get_similar_alerts(alert):
    similar_alerts = Alert.objects.filter(
        started_on__date=alert.started_on,
        hazard=alert.hazard
    ).exclude(id=alert.id)
    if alert.point:
        similar_alerts = similar_alerts.filter(
            point__distance_lte=(alert.point, D(km=5))
        )
    elif alert.polygon:
        similar_alerts = similar_alerts.filter(
            polygon__distance_lte=(alert.polygon, D(km=5))
        )
    else:
        return []
    return similar_alerts.order_by("-started_on")


def generate_polygon_from_wards(wards):
    polygon = GEOSGeometry(wards[0].boundary)
    if len(wards) > 1:
        for ward in wards[1:]:
            polygon = polygon.union(GEOSGeometry(ward.boundary))
        return MultiPolygon(polygon)
    return polygon


def get_alert_title(alert):
    location = None
    if alert.point:
        location = geocoder.google(
            [alert.point.y, alert.point.x],
            components="country:NP",
            method='reverse',
            key=GOOGLE_MAP_API_KEY,
        )
    if location and location.city:
        return "%s at %s" % (alert.hazard, location.city)
    else:
        return "%s" % alert.hazard


def alert_notification(alert):
    alerts = []
    alerts.append('<tr><td style="border: 1px solid black; border-collapse: collapse">%s</td>'
                  '<td style="border: 1px solid black; border-collapse: collapse">%s</td>'
                  '<td  style="border: 1px solid black; border-collapse: collapse">%s</td>'
                  '<td  style="border: 1px solid black; border-collapse: collapse">%s</td>'
                  '<td  style="border: 1px solid black; border-collapse: collapse">%s</td></tr>'
                  % (alert.source, alert.description, alert.hazard,
                     alert.started_on, alert.expire_on)
                  )

    email_message = """\
                <h3> %s </h3>
                <table style="width:700px; border:1px solid black; text-align: center; border-collapse: collapse;">
                <tr>
                <th style="border: 1px solid black; border-collapse: collapse">Source</th>
                <th style="border: 1px solid black; border-collapse: collapse">Description</th>
                <th style="border: 1px solid black; border-collapse: collapse">Hazard</th>
                <th style="border: 1px solid black; border-collapse: collapse">Started On</th>
                <th style="border: 1px solid black; border-collapse: collapse">Expire On</th>
                </tr>
                %s
                </table>
              """ % (alert.title, ''.join(alerts))
    return email_message
