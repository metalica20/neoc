import requests
from realtime.models import Pollution
from django.contrib.gis.geos import Point
from datetime import datetime


def fetch_pollution():
    response = requests.get('https://api.openaq.org/v1/latest?country=NP')
    pollution_data = response.json()
    pollutions = []
    for data in pollution_data['results']:
        measurements = []
        for i in range(0, len(data['measurements'])):
            measurement = [
                {
                    "parameter": data['measurements'][i]['parameter'],
                    "value":data['measurements'][i]['value'],
                    "unit":data['measurements'][i]['unit'],
                    "source":data['measurements'][i]['sourceName'],
                }
            ]
            measurements.append(measurement)
        pollution = Pollution(
            location=data['location'],
            city=data['city'],
            measured_on=datetime.strptime(data['measurements'][0]['lastUpdated'].split('.', 1)[0], '%Y-%m-%dT%H:%M:%S'),
            measurements=measurements,
            point=Point(float(data['coordinates']['longitude']), float(data['coordinates']['latitude'])),
        )
        pollutions.append(pollution)
    Pollution.objects.all().delete()
    Pollution.objects.bulk_create(pollutions)
