"""
Populate ward in Incident, Resource from point
"""
from django.core.management.base import BaseCommand
from django.db.models import OuterRef, Subquery
from incident.models import Incident
from resources.models import Resource
from federal.models import Ward


class Command(BaseCommand):

    def add_arguments(self, parser):

        parser.add_argument(
            '--incident',
            action='store_true',
            dest='incident',
            help='Populate incident',
        )
        parser.add_argument(
            '--resource',
            action='store_true',
            dest='resource',
            help='Populate resource',
        )

    def handle(self, **options):
        if options['incident']:
            incidents = Incident.objects.filter(wards=None)
            for incident in incidents:
                if incident.polygon:
                    wards = Ward.objects.filter(
                        boundary__contains=incident.polygon
                    )
                    incident.wards.set(wards)
                elif incident.point:
                    wards = Ward.objects.filter(
                        boundary__contains=incident.point
                    )
                    incident.wards.set(wards)
                incident.save()

        if options['resource']:
            Resource.objects.filter(ward=None).update(
                ward=Subquery(
                    Ward.objects.filter(
                        boundary__contains=OuterRef('point')
                    ).values('id')[:1]
                )
            )
