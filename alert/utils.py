from .models import Alert
from django.contrib.gis.measure import D


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
            polyon__distance_lte=(alert.polygon, D(km=5))
        )
    else:
        return []
    return similar_alerts.order_by("-started_on")
