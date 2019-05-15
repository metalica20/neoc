from incident.models import Incident
from hazard.models import Hazard


def update_incident():
    incidents = Incident.objects.all()
    for incident in incidents:
        hazard = Hazard.objects.filter(id=incident.hazard.id).first()
        if hazard.title.lower() not in incident.title.lower():
            hazard.title = incident.title.split(" at", 1)[0]
            hazard = Hazard.objects.filter(title__iexact=hazard.title).first()
            Incident.objects.filter(id=incident.id).update(hazard=hazard)