from django.core.management.base import BaseCommand
from incident.scripts.incident import fetch_incident


class Command(BaseCommand):
    help = 'Import incident data'

    def handle(self, **options):
        fetch_incident()
