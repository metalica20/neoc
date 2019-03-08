import shapefile
from resources.models import Health
from django.contrib.gis.geos import Point


def import_hospital():
    hospital_shape_file = shapefile.Reader("./health/HealthFacilities01Mar2017_v5.shp")
    hospital_data = hospital_shape_file.shapeRecords()

    for data in hospital_data:
        Health.objects.create(
                title=data.record['Name'],
                point=Point(float(data.record['Longitude']), float(data.record['Latitude'])),
                type=data.record['TYPE'],
                cbs_code=data.record['CBS_CODE']
        )

    major_hospital_shape_file = shapefile.Reader("healthhub/Hub_Hospital_Added_MUTM84.shp")
    major_hospital_data = major_hospital_shape_file.shapeRecords()

    for data in major_hospital_data:
        Health.objects.create(
                    title=data.record['Name'],
                    point=Point(float(data.record['Longitude']), float(data.record['Latitude'])),
                )

    medical_stores = shapefile.Reader("WHO/WHO_HEOC_PHEOC_Added_MUTM84.shp")
    medical_stores_data = medical_stores.shapeRecords()

    for medical_data in medical_stores_data:
        Health.objects.create(
            title=medical_data.record['HEOC_PHEOC'],
            point=Point(float(medical_data.record['Longitude']), float(medical_data.record['Latitude'])),
        )
