import csv
from django.core.management import BaseCommand
from resources.models import Health
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
                try:
                    Bank = Health.objects.create(
                    name=row[0],
                    operator_type=row[1],
                    opening_hours=row[2],
                    phone_number=row[3],
                    email_address=row[4],
                    emergency_service=row[5],
                    icu=row[6],
                    nicu=row[7],
                    operating_theatre=row[8],
                    x_ray=row[9],
                    ambulance_service=row[10],
                    number_of_staff=row[11],
                    number_of_Beds=row[12],
                    Comments=row[13],
                    type=row[14],
                    lat=row[16],
                    long=row[15],
                    location=Point(float(row[15]),float(row[16]))
                    )
                except:
                    print('error')
