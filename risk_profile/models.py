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
    location=models.PointField(null=True, blank=True, default=None,srid=32140)



class LayerTable(models.Model):
    CHOICES = (
    ('flood', 'Flood'),
    ('landslide', 'Landslide'),
    ('fire', 'Fire'),
    ('earthquake', 'Earthquake'),
    ('light', 'Lightening'),
    ('lights', 'Lightenings'),
)


    layer_name=models.CharField(max_length=250,null=True, blank=True, default=None)
    layer_tbl=models.CharField(max_length=250,null=True, blank=True, default=None)
    layer_icon=models.CharField(max_length=250,null=True, blank=True, default=None)
    layer_cat=models.CharField(max_length=250,null=True, blank=True, default=None)
    isGeoserver=models.BooleanField(null=True, blank=True, default=True)
    public=models.BooleanField(null=True, blank=True, default=True)
    visibility_level=models.CharField(max_length=250,null=True, blank=True, default=None)
    layer_type=models.CharField(max_length=250,null=True, blank=True, default=None)
    hazard=models.CharField(max_length=35, choices=CHOICES)
