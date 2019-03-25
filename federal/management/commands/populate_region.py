"""
Populate ward in Incident, Resource from point
"""
from django.core.management.base import BaseCommand
from django.db.models import OuterRef, Subquery
from incident.models import Incident
from resources.models import Resource
from federal.models import Ward


class Command(BaseCommand):

    def handle(self, **options):
        incidents = Incident.objects.all()
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

        Resource.objects.update(
            ward=Subquery(
                Ward.objects.filter(
                    boundary__contains=OuterRef('point')
                ).values('id')[:1]
            )
        )
