import requests
import datetime
from bs4 import BeautifulSoup
from realtime.models import Earthquake
from django.contrib.gis.geos import Point
from django.utils import timezone
from alert.models import Alert
from hazard.models import Hazard
from federal.models import Ward


url = "http://seismonepal.gov.np/earthquakes/2019"
table_selector = "tbody", {"id": "searchResultBody"}

fields = [
    "date",
    "time",
    "latitude",
    "longitude",
    "magnitude",
    "remarks",
    "location",
]


def scrape_earthquakes():
    """Scraping seismological data for different years from different places in Nepal"""
    rows = []

    r = requests.get(url)
    data = r.text
    soup = BeautifulSoup(data, "html.parser")
    earthquakes = soup.find(table_selector).find_all('tr')

    latest_event = datetime.datetime.fromtimestamp(0)
    latest_earthquake = Earthquake.objects.values('event_on').order_by('-event_on').first()

    if latest_earthquake:
        latest_event = latest_earthquake['event_on']
        latest_event = timezone.localtime(latest_event)
        latest_event = latest_event.replace(tzinfo=None)

    for earthquake in earthquakes:
        texts = earthquake.text.split("\n")
        rows.append(texts)
    for row in rows:
        while '' in row:
            row.remove('')
        earthquake = {}
        for i in range(0, len(fields)):
            earthquake[fields[i]] = row[i+1]
        earthquake['date'] = row[1][4:]
        earthquake['time'] = row[2][6:11]
        if earthquake['time'] == "N/A":
            earthquake['time'] = "00:00"
        event_on = datetime.datetime.strptime(earthquake['date'] + ' ' + earthquake['time'], '%Y-%m-%d %H:%M')
        if event_on > latest_event:
            earthquake = Earthquake(
                    event_on=event_on,
                    point=Point(float(earthquake['longitude']), float(earthquake['latitude'])),
                    magnitude=earthquake['magnitude'],
                    description=earthquake['remarks'],
                    address=earthquake['location'],
            )
            earthquake.save()
            create_alert(earthquake)


def create_alert(earthquake):
    if float(earthquake.magnitude) > 4:
        value = int(float(earthquake.magnitude)-3)
        alert_expiry = earthquake.event_on + datetime.timedelta(7*value)
        hazard = Hazard.objects.get(title="Earthquake")
        wards = Ward.objects.filter(boundary__intersects=earthquake.point)
        alert = Alert(
            title="Earthquake at %s" % earthquake.address,
            source="nsc",
            description="Earth of magnitude %s occurred at %s on %s"
                        % (earthquake.magnitude, earthquake.address, earthquake.event_on),
            hazard=hazard,
            public=True,
            verified=True,
            started_on=earthquake.event_on,
            expire_on=alert_expiry,
            point=earthquake.point,
        )
        alert.save()
        alert.wards.set(wards)