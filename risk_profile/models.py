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

    Bnktyp = (
    ('commercial', 'Commercial'),
    ('development', 'Development'),
    ('finance', 'Finance'),
    ('micro_credit_development', 'Micro Credit Development'),

)

    Optyp = (
    ('government', 'Government'),
    ('private', 'Private'),
    ('community', 'Community'),
    ('other', 'Other'),

)

    Yn = (
    ('yes', 'Yes'),
    ('no', 'No'),

)



    name=models.CharField(max_length=250,null=True, blank=True, default=None)
    phone_number=models.CharField(max_length=550,null=True, blank=True, default=None)
    email_address=models.CharField(max_length=550,null=True, blank=True, default=None)
    website=models.CharField(max_length=550,null=True, blank=True, default=None)
    opening_hours=models.CharField(max_length=550,null=True, blank=True, default=None)
    operator_type=models.CharField(max_length=50,choices=Optyp,null=True, blank=True, default=None)
    bank_type=models.CharField(max_length=50,choices=Bnktyp,null=True, blank=True, default=None)
    atm_available=models.CharField(max_length=50,choices=Yn,null=True, blank=True, default='no')
    Comments=models.CharField(max_length=550,null=True, blank=True, default=None)
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

# class Education(models.Model):
#     name=models.CharField(max_length=550,null=True, blank=True, default=None)
#     lat=models.CharField(max_length=250,null=True, blank=True, default=None)
#     long=models.CharField(max_length=250,null=True, blank=True, default=None)
#     location=models.PointField(null=True, blank=True, default=None)
#
#     def __str__(self):
#         return self.name


#new model as in sheets

class SocioEconomicGapanapa(models.Model):
    slug_id=models.CharField(max_length=500,null=True, blank=True, default=None)
    name=models.CharField(max_length=500,null=True, blank=True, default=None)
    gn_type=models.CharField(max_length=500,null=True, blank=True, default=None)
    district=models.CharField(max_length=500,null=True, blank=True, default=None)
    province=models.CharField(max_length=500,null=True, blank=True, default=None)
    no_facility_com=models.CharField(max_length=500,null=True, blank=True, default=None)
    one_atleast_com=models.CharField(max_length=500,null=True, blank=True, default=None)
    radio_com=models.CharField(max_length=500,null=True, blank=True, default=None)
    television_com=models.CharField(max_length=500,null=True, blank=True, default=None)
    cablet_com=models.CharField(max_length=500,null=True, blank=True, default=None)
    computer_com=models.CharField(max_length=500,null=True, blank=True, default=None)
    internet_com=models.CharField(max_length=500,null=True, blank=True, default=None)
    telegraph_com=models.CharField(max_length=500,null=True, blank=True, default=None)
    mobile_com=models.CharField(max_length=500,null=True, blank=True, default=None)
    wood_cook=models.CharField(max_length=500,null=True, blank=True, default=None)
    kerosene_cook=models.CharField(max_length=500,null=True, blank=True, default=None)
    lpgas_cook=models.CharField(max_length=500,null=True, blank=True, default=None)
    biogas_cook=models.CharField(max_length=500,null=True, blank=True, default=None)
    sa_cook=models.CharField(max_length=500,null=True, blank=True, default=None)
    electricity_cook=models.CharField(max_length=500,null=True, blank=True, default=None)
    other_cook=models.CharField(max_length=500,null=True, blank=True, default=None)
    nosta_cook=models.CharField(max_length=500,null=True, blank=True, default=None)
    electricity_light=models.CharField(max_length=500,null=True, blank=True, default=None)
    kerosene_light=models.CharField(max_length=500,null=True, blank=True, default=None)
    biogas_light=models.CharField(max_length=500,null=True, blank=True, default=None)
    solar_light=models.CharField(max_length=500,null=True, blank=True, default=None)
    other_light=models.CharField(max_length=500,null=True, blank=True, default=None)
    nons_light=models.CharField(max_length=500,null=True, blank=True, default=None)
    tap_water=models.CharField(max_length=500,null=True, blank=True, default=None)
    tube_water=models.CharField(max_length=500,null=True, blank=True, default=None)
    cok_water=models.CharField(max_length=500,null=True, blank=True, default=None)
    unco_water=models.CharField(max_length=500,null=True, blank=True, default=None)
    spou_water=models.CharField(max_length=500,null=True, blank=True, default=None)
    river_water=models.CharField(max_length=500,null=True, blank=True, default=None)
    other_water=models.CharField(max_length=500,null=True, blank=True, default=None)
    nots_water=models.CharField(max_length=500,null=True, blank=True, default=None)
    wit_toilet=models.CharField(max_length=500,null=True, blank=True, default=None)
    flush_toilet=models.CharField(max_length=500,null=True, blank=True, default=None)
    ordinary_toilet=models.CharField(max_length=500,null=True, blank=True, default=None)
    not_toilet=models.CharField(max_length=500,null=True, blank=True, default=None)




class Health(models.Model):

    Optyp = (
    ('government', 'Government'),
    ('private', 'Private'),
    ('community', 'Community'),
    ('other', 'Other'),

)

    Yn = (
    ('yes', 'Yes'),
    ('no', 'No'),

)



    name=models.CharField(max_length=550,null=True, blank=True, default=None)
    operator_type=models.CharField(max_length=50,choices=Optyp,null=True, blank=True, default=None)
    opening_hours=models.CharField(max_length=550,null=True, blank=True, default=None)
    phone_number=models.CharField(max_length=550,null=True, blank=True, default=None)
    email_address=models.CharField(max_length=550,null=True, blank=True, default=None)
    emergency_service=models.CharField(max_length=50,choices=Yn,default='no')
    icu=models.CharField(max_length=50,choices=Yn,default='no')
    nicu=models.CharField(max_length=50,choices=Yn,default='no')
    operating_theatre=models.CharField(max_length=50,default='no')
    x_ray=models.CharField(max_length=50,choices=Yn,default='no')
    ambulance_service=models.CharField(max_length=50,choices=Yn,default='no')
    number_of_staff=models.CharField(max_length=550,null=True, blank=True, default=None)
    number_of_Beds=models.CharField(max_length=550,null=True, blank=True, default=None)
    Comments=models.CharField(max_length=550,null=True, blank=True, default=None)
    type=models.CharField(max_length=550,null=True, blank=True, default=None)
    lat=models.CharField(max_length=250,null=True, blank=True, default=None)
    long=models.CharField(max_length=250,null=True, blank=True, default=None)
    location=models.PointField(null=True, blank=True, default=None)

    def __str__(self):
        return self.name



class Education(models.Model):

    Optyp = (
    ('government', 'Government'),
    ('private', 'Private'),
    ('community', 'Community'),

)


    name=models.CharField(max_length=550,null=True, blank=True, default=None)
    operator_type=models.CharField(max_length=50,choices=Optyp,null=True, blank=True, default=None)
    opening_hours=models.CharField(max_length=550,null=True, blank=True, default=None)
    phone_number=models.CharField(max_length=550,null=True, blank=True, default=None)
    email_address=models.CharField(max_length=550,null=True, blank=True, default=None)
    number_of_employees=models.CharField(max_length=550,null=True, blank=True, default=None)
    number_of_students=models.CharField(max_length=550,null=True, blank=True, default=None)
    comments=models.CharField(max_length=550,null=True, blank=True, default=None)
    type=models.CharField(max_length=550,null=True, blank=True, default=None)
    lat=models.CharField(max_length=250,null=True, blank=True, default=None)
    long=models.CharField(max_length=250,null=True, blank=True, default=None)
    location=models.PointField(null=True, blank=True, default=None)

    def __str__(self):
        return self.name



 #end   model used


#publish data model

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
    def type(self):
        # layer_tbl = get_object_or_404(obj.layer_tbl)
        try:
            # print('hello')
            return apps.get_model('risk_profile', self.layer_tbl).objects.values('type').distinct()

            # return  model_name.objects.all().count()
            # return getattr(models, obj.layer_tbl).objects.all()
        except Exception as e:
            print('error',e)
            return apps.get_model('risk_profile', self.layer_tbl).objects.none()

# end publish data model
