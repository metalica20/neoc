import requests
from pygeocoder import Geocoder
from django.contrib.gis.geos import Point
from hazard.models import Hazard
from incident.models import Incident
from loss.models import People, Loss, Family, Livestock, Infrastructure
import os

API_KEY = os.environ.get('GOOGLE_MAPS_API_KEY')


def fetch_incident():
    # fetch incident data from drr portal

    response = requests.get('http://drrportal.gov.np/signageapi/data.php')
    response_metadata = requests.get('http://drrportal.gov.np/signageapi/meta.php')

    meta_data = response_metadata.json()
    incident_data = response.json()

    for data in incident_data:

        if Incident.objects.filter(id=int(data['Incident ID'])).exists():
            continue

        try:
            loss = Loss.objects.create(
                estimated_loss=data['Estimated Loss']
            )
        except ValueError:
            loss = Loss.objects.create()

        incident_type = map_incident_type(data['Incident Type'], meta_data)
        title = get_address(float(data['Incident Latitude']), float(
            data['Incident Longitude']), incident_type)
        hazards = Hazard.objects.values('id', 'title')
        for hazard in hazards:
            if hazard['title'] == incident_type:
                hazard_id = hazard['id']

        if data['Reported By'] == "Nepal Police":
            source = "nepal_police"
        else:
            source = "other"

        try:
            point = Point(float(data['Incident Longitude']), float(data['Incident Latitude']))
        except TypeError:
            point = ""

        try:
            Incident.objects.create(
                id=data['Incident ID'],
                title=title,
                incident_on=data['Incident Date'],
                reported_on=data['Reported Datetime'],
                loss=loss,
                source_id=source,
                point=point,
                hazard_id=hazard_id,
                verified=True,
            )
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


def get_address(lat, long, incident_type):
    location = Geocoder(API_KEY).reverse_geocode(lat, long)
    if location.city:
        return incident_type + " at " + location.city
    else:
        return incident_type
