from django.contrib.gis.db import models
from django.apps import apps



# Create your models here.
class Hospital(models.Model):
    lat=models.CharField(max_length=250,null=True, blank=True, default=None)
    long=models.CharField(max_length=250,null=True, blank=True, default=None)
    fid=models.CharField(max_length=250,null=True, blank=True, default=None)
    name=models.CharField(max_length=250,null=True, blank=True, default=None)
    district=models.CharField(max_length=250,null=True, blank=True, default=None)
    vdc=models.CharField(max_length=250,null=True, blank=True, default=None)
    ward=models.CharField(max_length=250,null=True, blank=True, default=None)
    type=models.CharField(max_length=250,null=True, blank=True, default=None)
    location=models.PointField(null=True, blank=True, default=None)

    def __str__(self):
        return self.name

class School(models.Model):
    name=models.CharField(max_length=250)
    lat=models.CharField(max_length=250)
    long=models.CharField(max_length=250)
    location=models.PointField(null=True, blank=True, default=None,srid=32140)


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

    def __str__(self):
        return self.name


class Bank(models.Model):
    name=models.CharField(max_length=250,null=True, blank=True, default=None)
    lat=models.CharField(max_length=250,null=True, blank=True, default=None)
    long=models.CharField(max_length=250,null=True, blank=True, default=None)
    location=models.PointField(null=True, blank=True, default=None)

    def __str__(self):
        return self.name


class Settlements(models.Model):
    name=models.CharField(max_length=250,null=True, blank=True, default=None)
    type=models.CharField(max_length=250,null=True, blank=True, default=None)
    lat=models.CharField(max_length=250,null=True, blank=True, default=None)
    long=models.CharField(max_length=250,null=True, blank=True, default=None)
    location=models.PointField(null=True, blank=True, default=None)

    def __str__(self):
        return self.name

class Airport(models.Model):
    name=models.CharField(max_length=250,null=True, blank=True, default=None)
    lat=models.CharField(max_length=250,null=True, blank=True, default=None)
    long=models.CharField(max_length=250,null=True, blank=True, default=None)
    location=models.PointField(null=True, blank=True, default=None)

    def __str__(self):
        return self.name

class Bridge(models.Model):
    name=models.CharField(max_length=250,null=True, blank=True, default=None)
    lat=models.CharField(max_length=250,null=True, blank=True, default=None)
    long=models.CharField(max_length=250,null=True, blank=True, default=None)
    location=models.PointField(null=True, blank=True, default=None)

    def __str__(self):
        return self.name


class Policestation(models.Model):
    name=models.CharField(max_length=250,null=True, blank=True, default=None)
    lat=models.CharField(max_length=250,null=True, blank=True, default=None)
    long=models.CharField(max_length=250,null=True, blank=True, default=None)
    location=models.PointField(null=True, blank=True, default=None)

    def __str__(self):
        return self.name

class Education(models.Model):
    name=models.CharField(max_length=550,null=True, blank=True, default=None)
    lat=models.CharField(max_length=250,null=True, blank=True, default=None)
    long=models.CharField(max_length=250,null=True, blank=True, default=None)
    location=models.PointField(null=True, blank=True, default=None)

    def __str__(self):
        return self.name

class LayerTable(models.Model):

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
    geoserver_url=models.CharField(max_length=250,null=True, blank=True, default=None)
    geoserver_workspace=models.CharField(max_length=250,null=True, blank=True, default=None)
    public=models.BooleanField(null=True, blank=True, default=True)
    visibility_level=models.CharField(max_length=250,choices=Visibility,null=True, blank=True, default=None)
    layer_type=models.CharField(max_length=250,choices=Layertype,null=True, blank=True, default=None)
    sub_category=models.CharField(max_length=500,null=True, blank=True, default=None)
    upload_type=models.CharField(max_length=50,choices=Uploadtype,null=True, blank=True, default=None)


    def __str__(self):
        return self.layer_name

    def list_string(self):
        try:
            aa=  self.sub_category.split(',')
        except:
            aa=[]
        return aa
    def count_obj(self):
        # layer_tbl = get_object_or_404(obj.layer_tbl)
        try:
            # print('hello')
            return apps.get_model('risk_profile', self.layer_tbl).objects.all().count()

            # return  model_name.objects.all().count()
            # return getattr(models, obj.layer_tbl).objects.all()
        except Exception as e:
            print('error',e)
            return 0
        # return layer_tbl.count()
