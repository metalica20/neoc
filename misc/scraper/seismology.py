import requests
import datetime
from bs4 import BeautifulSoup
from realtime.models import Earthquake
from django.contrib.gis.geos import Point
from django.utils import timezone

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
    article = soup.find(table_selector).find_all('tr')

    latest_event = datetime.datetime.fromtimestamp(0)
    latest_earthquake = Earthquake.objects.values('event_on').order_by('-event_on').first()

    if latest_earthquake:
        latest_event = latest_earthquake['event_on']
        latest_event = timezone.localtime(latest_event)
        latest_event = latest_event.replace(tzinfo=None)

    for element in article:
        texts = element.text.split("\n")
        rows.append(texts)
    for row in rows:
        earthquake = {}
        for i in range(0, len(fields)):
            earthquake[fields[i]] = row[i+1]

        earthquake['date'] = row[1][4:]
        earthquake['time'] = row[2][5:]
        if earthquake['time'] == "N/A":
            earthquake['time'] = "00:00"
        event_on = datetime.datetime.strptime(earthquake['date'] + ' ' + earthquake['time'], '%Y-%m-%d %H:%M')

        if event_on > latest_event:
            Earthquake.objects.create(
                    event_on=event_on,
                    point=Point(float(earthquake['longitude']), float(earthquake['latitude'])),
                    magnitude=earthquake['magnitude'],
                    description=earthquake['remarks'],
                    address=earthquake['location'],
            )
