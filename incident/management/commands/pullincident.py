from django.core.management.base import BaseCommand
from incident.scripts.incident import fetch_incident


class Command(BaseCommand):
    help = 'Import incident data'

    def add_arguments(self, parser):

        parser.add_argument(
            '--historical',
            action='store_true',
            dest='historical',
            help='Import historical data',
        )
        parser.add_argument(
            '--all',
            action='store_true',
            dest='all',
            help='Import all data',
        )

    def handle(self, **options):
        fetch_incident(options)
