import requests
import geocoder
from django.contrib.gis.geos import Point
from hazard.models import Hazard
from incident.models import Incident
from loss.models import People, Loss, Family, Livestock, Infrastructure
import os
from federal.models import Ward

GOOGLE_MAP_API_KEY = os.environ.get('GOOGLE_MAPS_API_KEY')

CURRENT_INCIDENT_URL = 'http://drrportal.gov.np/signageapi/data.php'
ALL_INCIDENT_URL = 'http://drrportal.gov.np/signageapi/all.php'
HISTORICAL_INCIDENT_URL = 'http://drrportal.gov.np/signageapi/all2010.php'
META_URL = 'http://drrportal.gov.np/signageapi/meta.php'


def fetch_incident(options):
    # fetch incident data from drr portal

    INCIDENT_URL = CURRENT_INCIDENT_URL
    old = False

    if(options['all']):
        INCIDENT_URL = ALL_INCIDENT_URL
    elif(options['historical']):
        INCIDENT_URL = HISTORICAL_INCIDENT_URL
        old = True

    response = requests.get(INCIDENT_URL)
    response_metadata = requests.get(META_URL)

    meta_data = response_metadata.json()
    incident_data = response.json()

    for data in incident_data:

        if Incident.objects.filter(id=int(data['Incident ID'])).exists():
            continue
        if not data['Incident Latitude']:
            continue

        try:
            loss = Loss.objects.create(
                estimated_loss=data['Estimated Loss']
            )
        except ValueError:
            loss = Loss.objects.create()

        incident_type = map_incident_type(data['Incident Type'], meta_data)
        title = get_title(float(data['Incident Latitude']), float(
            data['Incident Longitude']), incident_type)
        hazard = Hazard.objects.filter(title__iexact=incident_type).first()
        if not hazard:
            hazard = Hazard.objects.filter(id=45).first()
        if data['Reported By'] == "Nepal Police":
            source = "nepal_police"
        else:
            source = "other"

        try:
            point = Point(float(data['Incident Longitude']), float(data['Incident Latitude']))
        except TypeError:
            point = ""

        try:
            wards = Ward.objects.filter(boundary__intersects=point)
            incident = Incident.objects.create(
                id=data['Incident ID'],
                title=title,
                incident_on=data['Incident Date'],
                reported_on=data['Reported Datetime'],
                street_address=data['Incident Place'],
                loss=loss,
                source_id=source,
                point=point,
                hazard=hazard,
                verified=True,
                approved=True,
                old=old,
            )
            incident.wards.set(wards)
        except:
            continue

        if int(data['Death Male']) > 0:
            People.objects.create(
                loss=loss,
                status="dead",
                gender="male",
                count=data['Death Male']
            )
        if int(data['Death Female']) > 0:
            People.objects.create(
                loss=loss,
                status="dead",
                gender="female",
                count=data['Death Female']
            )
        if int(data['Death Unknown']) > 0:
            People.objects.create(
                loss=loss,
                status="dead",
                count=data['Death Unknown']
            )
        if int(data['Injured Male']) > 0:
            People.objects.create(
                loss=loss,
                status="injured",
                gender="male",
                count=data['Injured Male']
            )
        if int(data['Injured Female']) > 0:
            People.objects.create(
                loss=loss,
                status="injured",
                gender="female",
                count=data['Injured Female']
            )
        if int(data['Missing People']) > 0:
            People.objects.create(
                loss=loss,
                status="missing",
                count=data['Missing People']
            )

        if int(data['Affected Family']) > 0:
            Family.objects.create(
                loss=loss,
                status="affected",
                count=data['Affected Family']
            )
        if int(data['Displaced Family']) > 0:
            Family.objects.create(
                loss=loss,
                status="relocated",
                count=data['Displaced Family']
            )

        if int(data['Animal Loss']) > 0:
            Livestock.objects.create(
                loss=loss,
                type_id='1',
                status="destroyed",
                count=data['Animal Loss']
            )

        if int(data['Complete damage (House)']) > 0:
            Infrastructure.objects.create(
                loss=loss,
                type_id='1',
                status="destroyed",
                count=data['Complete damage (House)']
            )
        if int(data['Partial damage (House)']) > 0:
            Infrastructure.objects.create(
                loss=loss,
                type_id='1',
                status="affected",
                count=data['Partial damage (House)']
            )


def map_incident_type(incident_id, meta_data):
    for data in meta_data['incidenttype']:
        if data[0] == incident_id:
            return data[1]


def get_title(lat, long, incident_type):
    location = geocoder.google([lat, long], components="country:NP", method='reverse', key=GOOGLE_MAP_API_KEY)
    if location.city:
        return incident_type + " at " + location.city
    else:
        return incident_type
