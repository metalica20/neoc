from django.core.management.base import BaseCommand
from incident.scripts.updateincident import update_incident


class Command(BaseCommand):
    help = 'Update incident from database'

    def handle(self, **options):
        update_incident()
