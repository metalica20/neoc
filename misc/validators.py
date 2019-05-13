import os
import json
from django.core.exceptions import ValidationError
from django.contrib.gis.geos import GEOSGeometry
from django.utils.translation import ugettext_lazy as _


def validate_geojson(value):
    extension = os.path.splitext(value.name)[1]
    valid_extensions = ['.json', '.geojson']
    if not extension.lower() in valid_extensions:
        raise ValidationError(_('Upload files with extension .json or .geojson only'))
    geojson = json.loads(value.read().decode('utf-8'))
    if geojson['type'] != "Feature":
        raise ValidationError(_("Geojson type must be feature"))
    if geojson['geometry']['type'] != "MultiPolygon":
        raise ValidationError(_("Geometry type should be MultiPolygon"))
    if not GEOSGeometry(json.dumps(geojson['geometry'])):
        raise ValidationError(_("Invalid GeoJson"))
    value.seek(0)