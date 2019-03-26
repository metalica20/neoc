from misc.scraper.seismology import scrape_earthquakes
from realtime.scripts.rain import fetch_rain
from realtime.scripts.river import fetch_river
from realtime.scripts.pollution import fetch_pollution
from celery import shared_task


@shared_task
def fetch_earthquake_data():
    scrape_earthquakes()


@shared_task
def fetch_river_data():
    fetch_river()


@shared_task
def fetch_rain_data():
    fetch_rain()


@shared_task
def fetch_pollution_data():
    fetch_pollution()
