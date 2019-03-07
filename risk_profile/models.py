from django.contrib.gis.db import models


# Create your models here.
class Hospital(models.Model):
    fid=models.CharField(max_length=250,null=True, blank=True, default=None)
    name=models.CharField(max_length=250,null=True, blank=True, default=None)
    district=models.CharField(max_length=250,null=True, blank=True, default=None)
    vdc=models.CharField(max_length=250,null=True, blank=True, default=None)
    ward=models.CharField(max_length=250,null=True, blank=True, default=None)
    type=models.CharField(max_length=250,null=True, blank=True, default=None)
    lat=models.CharField(max_length=250,null=True, blank=True, default=None)
    long=models.CharField(max_length=250,null=True, blank=True, default=None)
    location=models.PointField(null=True, blank=True, default=None)

class School(models.Model):
    name=models.CharField(max_length=250)
    lat=models.CharField(max_length=250)
    long=models.CharField(max_length=250)
    location=models.PointField(null=True, blank=True, default=None)


class MarketCenter(models.Model):
    fid=models.CharField(max_length=250,null=True, blank=True, default=None)
    name=models.CharField(max_length=250,null=True, blank=True, default=None)
    district=models.CharField(max_length=250,null=True, blank=True, default=None)
    vdc=models.CharField(max_length=250,null=True, blank=True, default=None)
    ward=models.CharField(max_length=250,null=True, blank=True, default=None)
    wholesale=models.CharField(max_length=250,null=True, blank=True, default=None)
    commodity=models.CharField(max_length=250,null=True, blank=True, default=None)
    lat=models.CharField(max_length=250,null=True, blank=True, default=None)
    long=models.CharField(max_length=250,null=True, blank=True, default=None)
    location=models.PointField(null=True, blank=True, default=None)






class LayerTable(models.Model):
    CHOICES = (
    ('flood', 'Flood'),
    ('landslide', 'Landslide'),
    ('fire', 'Fire'),
    ('earthquake', 'Earthquake'),
    ('light', 'Lightening'),
    ('lights', 'Lightenings'),
)
    Visibility = (
    ('national', 'National'),
    ('local', 'Local Government'),

)
    Layertype = (
    ('vector', 'Vector'),
    ('raster', 'Raster'),

)

    Uploadtype = (
    ('csv', 'Csv'),
    ('shapefile', 'Shapefile'),
    ('geojson', 'Geojson'),
    ('geoserver', 'Geoserver'),

)

    Layercat = (
    ('hazard', 'Hazard'),
    ('vulnerability', 'Vulnerability'),
    ('resource', 'Capacity & Resources'),
    ('exposure', 'Exposure'),

)

    layer_name=models.CharField(max_length=250,null=True, blank=True, default=None)
    layer_tbl=models.CharField(max_length=250,null=True, blank=True, default=None)
    layer_icon=models.CharField(max_length=250,null=True, blank=True, default=None)
    layer_cat=models.CharField(max_length=250,choices=Layercat,null=True, blank=True, default=None)
    isGeoserver=models.BooleanField(null=True, blank=True, default=True)
    public=models.BooleanField(null=True, blank=True, default=True)
    visibility_level=models.CharField(max_length=250,choices=Visibility,null=True, blank=True, default=None)
    layer_type=models.CharField(max_length=250,choices=Layertype,null=True, blank=True, default=None)
    hazard=models.CharField(max_length=35, choices=CHOICES,null=True, blank=True, default=None)
    upload_type=models.CharField(max_length=50,choices=Uploadtype,null=True, blank=True, default=None)
