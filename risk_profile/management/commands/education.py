import csv
from django.core.management import BaseCommand
from risk_profile.models import Education
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
                if(row[10]!='long'):


                # print(row[2])
                    try:
                        education = Education.objects.create(
                        name=row[0],
                        operator_type=row[1],
                        opening_hours=row[2],
                        phone_number=row[3],
                        email_address=row[4],
                        number_of_employees=row[5],
                        number_of_students=row[6],
                        comments=row[7],
                        type=row[8],
                        lat=row[9],
                        long=row[10],
                        location=Point(float(row[10]),float(row[9]))
                        )
                    except:
                        print('error')
