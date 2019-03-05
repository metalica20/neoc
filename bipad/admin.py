from django.contrib.gis import admin, forms
from django.contrib.gis.db import models


class OSMWidget(forms.OSMWidget):
    default_lat = 28.3949
    default_lon = 84.1240
    default_zoom = 6


class GeoModelAdmin(admin.ModelAdmin):
    formfield_overrides = {
        models.MultiPolygonField: {'widget': OSMWidget},
        models.PolygonField: {'widget': OSMWidget},
        models.PointField: {'widget': OSMWidget},
    }
