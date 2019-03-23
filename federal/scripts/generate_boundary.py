"""
Generate municipality, district and province boundary from wards boundary
"""
from django.contrib.gis.geos.collections import MultiPolygon
from django.contrib.gis.db.models import (
    Union,
)
from federal.models import (
    Municipality,
    District,
    Province,
)


def generate_boundary():
    municipalities = Municipality.objects.annotate(
        n_boundary=Union(
            'wards__boundary'
        )
    ).all()
    save_boundary(municipalities)

    districts = District.objects.annotate(
        n_boundary=Union(
            'municipalities__boundary'
        )
    ).all()
    save_boundary(districts)

    provinces = Province.objects.annotate(
        n_boundary=Union(
            'districts__boundary'
        )
    ).all()
    save_boundary(provinces)


def save_boundary(instances):
    for instance in instances:
        try:
            if isinstance(instance.n_boundary, MultiPolygon):
                instance.boundary = instance.n_boundary
            else:
                instance.boundary = MultiPolygon(instance.n_boundary)
            instance.save()
        except Exception as e:
            print(e)
            print(instance, type(instance.n_boundary))
