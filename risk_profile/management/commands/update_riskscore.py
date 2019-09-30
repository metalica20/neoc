import csv
from django.core.management import BaseCommand
from risk_profile.models import DistrictLevelVulnerability
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
                    # Bank = DistrictLevelVulnerability.objects.create(
                    # district_id=row[0],
                    # province_id=row[1],
                    # district=row[2],
                    # remoteness=row[3],
                    # hdi=row[4],
                    # riskScore=row[5],
                    # perCapitaIncome=row[6],
                    # lifeExpectancy=row[7],
                    # humanPovertyIndex=row[8],
                    # )
                    if(row[1] == 'Risk_Score'):
                        print('1st row')
                    else:
                        print(row[0])
                        risk_update = DistrictLevelVulnerability.objects.filter(
                            district_id=row[0]).update(riskScore=float(row[1]))

                        print('updated succcesfully')

                except Exception as e:
                    print(e)
