from django.core.management.base import BaseCommand
from realtime.scripts.river import fetch_river


class Command(BaseCommand):
    help = 'Import river data from DHM api'

    def handle(self, **options):
        fetch_river()
