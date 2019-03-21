from django.contrib.gis import admin, forms
from polymorphic.admin import PolymorphicParentModelAdmin
from django.contrib.gis.db import models
from mapwidgets.widgets import GooglePointFieldWidget


class OSMWidget(forms.OSMWidget):
    default_lat = 28.3949
    default_lon = 84.1240
    default_zoom = 6


class GeoModelAdmin(admin.ModelAdmin):
    formfield_overrides = {
        models.MultiPolygonField: {'widget': OSMWidget},
        models.PolygonField: {'widget': OSMWidget},
        models.PointField: {'widget': GooglePointFieldWidget},
    }

    class Media:
        js = (
            'bipad/js/fix_map.js',
            'https://code.jquery.com/jquery-3.3.1.min.js',
        )


class GeoPolymorphicParentModelAdmin(PolymorphicParentModelAdmin):
    formfield_overrides = {
        models.MultiPolygonField: {'widget': OSMWidget},
        models.PolygonField: {'widget': OSMWidget},
        models.PointField: {'widget': OSMWidget},
    }

    class Media:
        js = (
            'bipad/js/fix_map.js',
            'https://code.jquery.com/jquery-3.3.1.min.js',
        )


