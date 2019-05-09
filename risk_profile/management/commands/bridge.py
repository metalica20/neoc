import csv
from django.core.management import BaseCommand
from risk_profile.models import Bridge
from django.contrib.gis.geos import GEOSGeometry
from django.contrib.gis.geos import Point

class Command(BaseCommand):
    help = 'Load a questions csv file into the database'

    def add_arguments(self, parser):
        parser.add_argument('--path', type=str)

    def handle(self, *args, **kwargs):
        path = kwargs['path']
        with open(path, 'rt') as f:
            reader = csv.reader(f, dialect='excel')
            # print(reader)

            for row in reader:
                # print(row[2])
                if(row[1]!='xcoord'):
                    bridge = Bridge.objects.create(
                        name=row[0],
                        # district=row[1],
                        lat=row[2],
                        long=row[1],
                        location=Point(float(row[1]),float(row[2]))



                )
