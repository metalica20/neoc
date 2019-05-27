from django.contrib.gis.db import models
from django.apps import apps
from django_pgviews import view as pg
from django.contrib.postgres.fields import JSONField


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


#test model

class Testw(models.Model):
    name=models.IntegerField(null=True, blank=True, default=None)


#new model as in sheets

class SocioEconomicGapanapa(models.Model):
    slug_id=models.CharField(max_length=500,null=True, blank=True, default=None)
    province_id=models.CharField(max_length=500,null=True, blank=True, default=None)
    district_id=models.CharField(max_length=500,null=True, blank=True, default=None)
    municipality_id=models.CharField(max_length=500,null=True, blank=True, default=None)
    name=models.CharField(max_length=500,null=True, blank=True, default=None)
    gn_type=models.CharField(max_length=500,null=True, blank=True, default=None)
    district=models.CharField(max_length=500,null=True, blank=True, default=None)
    province=models.CharField(max_length=500,null=True, blank=True, default=None)
    no_facility_com=models.IntegerField(null=True, blank=True, default=None)
    one_atleast_com=models.IntegerField(null=True, blank=True, default=None)
    radio_com=models.IntegerField(null=True, blank=True, default=None)
    television_com=models.IntegerField(null=True, blank=True, default=None)
    cablet_com=models.IntegerField(null=True, blank=True, default=None)
    computer_com=models.IntegerField(null=True, blank=True, default=None)
    internet_com=models.IntegerField(null=True, blank=True, default=None)
    telephone_com=models.IntegerField(null=True, blank=True, default=None)
    mobile_com=models.IntegerField(null=True, blank=True, default=None)
    wood_cook=models.IntegerField(null=True, blank=True, default=None)
    kerosene_cook=models.IntegerField(null=True, blank=True, default=None)
    lpgas_cook=models.IntegerField(null=True, blank=True, default=None)
    biogas_cook=models.IntegerField(null=True, blank=True, default=None)
    sa_cook=models.IntegerField(null=True, blank=True, default=None)
    electricity_cook=models.IntegerField(null=True, blank=True, default=None)
    other_cook=models.IntegerField(null=True, blank=True, default=None)
    nosta_cook=models.IntegerField(null=True, blank=True, default=None)
    electricity_light=models.IntegerField(null=True, blank=True, default=None)
    kerosene_light=models.IntegerField(null=True, blank=True, default=None)
    biogas_light=models.IntegerField(null=True, blank=True, default=None)
    solar_light=models.IntegerField(null=True, blank=True, default=None)
    other_light=models.IntegerField(null=True, blank=True, default=None)
    nons_light=models.IntegerField(null=True, blank=True, default=None)
    tap_water=models.IntegerField(null=True, blank=True, default=None)
    tube_water=models.IntegerField(null=True, blank=True, default=None)
    cok_water=models.IntegerField(null=True, blank=True, default=None)
    unco_water=models.IntegerField(null=True, blank=True, default=None)
    spou_water=models.IntegerField(null=True, blank=True, default=None)
    river_water=models.IntegerField(null=True, blank=True, default=None)
    other_water=models.IntegerField(null=True, blank=True, default=None)
    nots_water=models.IntegerField(null=True, blank=True, default=None)
    wit_toilet=models.IntegerField(null=True, blank=True, default=None)
    flush_toilet=models.IntegerField(null=True, blank=True, default=None)
    ordinary_toilet=models.IntegerField(null=True, blank=True, default=None)
    not_toilet=models.IntegerField(null=True, blank=True, default=None)




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


class Risk(models.Model):
    district_id=models.CharField(max_length=550,null=True, blank=True, default=None)
    province_id=models.CharField(max_length=550,null=True, blank=True, default=None)
    district=models.CharField(max_length=550,null=True, blank=True, default=None)
    remoteness=models.FloatField(null=True, blank=True, default=None)
    hdi=models.FloatField(null=True, blank=True, default=None)
    riskScore=models.FloatField(null=True, blank=True, default=None)
    perCapitaIncome=models.FloatField(null=True, blank=True, default=None)
    lifeExpectancy=models.FloatField(null=True, blank=True, default=None)
    humanPovertyIndex=models.FloatField(null=True, blank=True, default=None)

    def __str__(self):
        return self.district


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
            return apps.get_model('resources', self.layer_tbl).objects.all().count()

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
            return apps.get_model('resources', self.layer_tbl).objects.values('type').distinct()

            # return  model_name.objects.all().count()
            # return getattr(models, obj.layer_tbl).objects.all()
        except Exception as e:
            print('error',e)
            return apps.get_model('resources', self.layer_tbl).objects.none()



class Healthv(pg.View):
    sql = """SELECT r.title,r.description,r.point,resources_health.* FROM resources_health LEFT JOIN resources_resource as r ON r.id=resources_health.resource_ptr_id;"""

    class Meta:
        db_table = 'health_views'
        managed = False

class Educationv(pg.View):
    sql = """SELECT r.title,r.description,r.point,resources_education.* FROM resources_education LEFT JOIN resources_resource as r ON r.id=resources_education.resource_ptr_id;"""

    class Meta:
        db_table = 'education_views'
        managed = False

class Financev(pg.View):
    sql = """SELECT r.title,r.description,r.point,resources_finance.* FROM resources_finance LEFT JOIN resources_resource as r ON r.id=resources_finance.resource_ptr_id;"""

    class Meta:
        db_table = 'finance_views'
        managed = False

class Governancev(pg.View):
    sql = """SELECT r.title,r.description,r.point,resources_governance.* FROM resources_governance LEFT JOIN resources_resource as r ON r.id=resources_governance.resource_ptr_id;"""

    class Meta:
        db_table = 'governance_views'
        managed = False

class Culturalv(pg.View):
    sql = """SELECT r.title,r.description,r.point,resources_cultural.* FROM resources_cultural LEFT JOIN resources_resource as r ON r.id=resources_cultural.resource_ptr_id;"""

    class Meta:
        db_table = 'cultural_views'
        managed = False



LICENSE_TYPES=(
    ('0', 'Survey'),
    ('1', 'Generation'),
    ('2', 'Operation'),
    )


def get_years():
    years = []
    for year in range(0000, 2081):
        years.append((year, year))
    return years

def get_months():
    months = []
    for month in range(0, 13):
        months.append((month, month))
    return sorted(months, reverse=True)

def get_days():
    days = []
    for day in range(0, 33):
        days.append((day, day))
    return sorted(days, reverse=True)



class Hydropower(models.Model):
    province = models.CharField(max_length=50, null=True, blank=True)
    district = models.CharField(max_length=50, null=True, blank=True)
    gapanapa = models.CharField(max_length=50, null=True, blank=True)
    province_name = models.CharField(max_length=50, null=True, blank=True)
    district_name = models.CharField(max_length=50, null=True, blank=True)
    gapanapa_name = models.CharField(max_length=100, null=True, blank=True)
    name = models.CharField(max_length=200)
    capacity = models.FloatField(verbose_name="Capacity (MW)", null=True, blank=True)
    river = models.CharField(max_length=100)
    lic_number = models.CharField(max_length=100, null=True, blank=True)    
    issue_date_years = models.IntegerField(default=0000, null=True, choices=get_years())
    issue_date_months = models.IntegerField(default=0, null=True, choices=get_months())
    issue_date_days = models.IntegerField(default=0, null=True, choices=get_days())    
    validity_date_years = models.IntegerField(default=0000, null=True, choices=get_years())
    validity_date_months = models.IntegerField(default=0, null=True, choices=get_months())
    validity_date_days = models.IntegerField(default=0, null=True, choices=get_days())
    promoter = models.CharField(max_length=200)
    address = models.CharField(max_length=200) 
    latlong = models.PointField(null=True, blank=True)
    license_type = models.CharField(max_length=15, choices=LICENSE_TYPES, default=0)
    about_project = models.TextField(blank=True)
    affected_households = models.CharField(max_length=100, null=True, blank=True)
    population_distribution = models.CharField(max_length=100, null=True, blank=True)
    migration_pattern = models.CharField(max_length=100, null=True, blank=True)
    age_group_distribution = models.CharField(max_length=100, null=True, blank=True)
    gender = models.BooleanField(default=True)
    ethnicity_and_religion = models.CharField(max_length=100, null=True, blank=True)
    literacy_rates = models.CharField(max_length=10, null=True, blank=True)
    skills_and_skilled_manpower = models.CharField(max_length=100, null=True, blank=True)
    health_post_sub_health_post_hospitals = models.CharField(max_length=100, null=True, blank=True)
    incidence_of_water_borne_and_infectious_diseases = models.CharField(max_length=100, null=True, blank=True)
    land_holding_size_ownership = models.CharField(max_length=100, null=True, blank=True)
    drinking_water_supply = models.CharField(max_length=100, null=True, blank=True)
    irrigation_canals = models.CharField(max_length=100, null=True, blank=True)
    foot_trails = models.CharField(max_length=100, null=True, blank=True)
    transportation = models.CharField(max_length=100, null=True, blank=True)
    electricity = models.CharField(max_length=100, null=True, blank=True)
    tele_communication = models.CharField(max_length=100, null=True, blank=True)
    historical_places = models.CharField(max_length=100, null=True, blank=True)
    public_spaces = models.CharField(max_length=100, null=True, blank=True)
    religious_cultural_sites = models.CharField(max_length=100, null=True, blank=True)
    government_agencies = models.CharField(max_length=100, null=True, blank=True)
    non_government_agencies = models.CharField(max_length=100, null=True, blank=True)
    cooperatives = models.CharField(max_length=100, null=True, blank=True)
    community_based_organization = models.CharField(max_length=100, null=True, blank=True)
    crooping_pattern_and_production = models.CharField(max_length=100, null=True, blank=True)
    livestock_raising = models.CharField(max_length=100, null=True, blank=True)
    loss_of_crops_production_by_crop_type_area_value = models.CharField(max_length=100, null=True, blank=True)
    land_price_information = models.CharField(max_length=100, null=True, blank=True)
    agriculture_and_forest_products = models.CharField(max_length=100, null=True, blank=True)
    occupation_and_employment = models.CharField(max_length=100, null=True, blank=True)
    agriculture_production = models.CharField(max_length=100, null=True, blank=True)
    livestock_production = models.CharField(max_length=100, null=True, blank=True)
    timber_forest_production = models.CharField(max_length=100, null=True, blank=True)
    non_timber_forest_production = models.CharField(max_length=100, null=True, blank=True)    
    trade_and_commerce = models.CharField(max_length=100, null=True, blank=True)
    area_map = models.CharField(max_length=100, null=True, blank=True)
    landholding_size_and_number = models.CharField(max_length=100, null=True, blank=True)
    measurement_of_house = models.CharField(max_length=100, null=True, blank=True)
    valuation_of_house = models.CharField(max_length=100, null=True, blank=True)
    valuation_of_cowshed = models.CharField(max_length=100, null=True, blank=True)
    valuation_of_other_structures = models.CharField(max_length=100, null=True, blank=True)
    land_compensation_rates = models.CharField(max_length=100, null=True, blank=True)
    agriculture_products_compensation_rates = models.CharField(max_length=100, null=True, blank=True)
    compensation_rates_of_forest =  models.CharField(max_length=100, null=True, blank=True)
    compensation_rates_of_house_private_structures = models.CharField(max_length=100, null=True, blank=True)
    maximum_temperature = models.CharField(max_length=100, null=True, blank=True)
    minimum_temperature = models.CharField(max_length=100, null=True, blank=True)
    rainfall_of_project_area = models.CharField(max_length=100, null=True, blank=True)
    altitude = models.CharField(max_length=100, null=True, blank=True)
    landscape = models.CharField(max_length=100, null=True, blank=True)
    air_quality = models.CharField(max_length=100, null=True, blank=True)
    water_quality = models.CharField(max_length=100, null=True, blank=True)
    noise_quality = models.CharField(max_length=100, null=True, blank=True)
    physiographic_location = models.CharField(max_length=100, null=True, blank=True)
    river_system_basin = models.CharField(max_length=100, null=True, blank=True)
    rock_type = models.CharField(max_length=100, null=True, blank=True)
    soil_type = models.CharField(max_length=100, null=True, blank=True)
    slope_stability = models.CharField(max_length=100, null=True, blank=True)
    erosion = models.CharField(max_length=100, null=True, blank=True)
    landslides = models.CharField(max_length=100, null=True, blank=True)
    land_use_pattern = models.CharField(max_length=100, null=True, blank=True)
    disaster_index_history = models.CharField(max_length=100, null=True, blank=True)
    food_index_history = models.CharField(max_length=100, null=True, blank=True)
    wildlife_bird_reserve = models.CharField(max_length=100, null=True, blank=True)
    distance_from_conservetion_area = models.CharField(max_length=100, null=True, blank=True)
    forest_type = models.CharField(max_length=100, null=True, blank=True)
    vegetation_area_type = models.CharField(max_length=100, null=True, blank=True)
    survey_licensed_obtained = models.CharField(max_length=100, null=True, blank=True)
    completed_survey_design = models.CharField(max_length=100, null=True, blank=True)
    available_location_map = models.CharField(max_length=100, null=True, blank=True)
    land_acquisition = models.CharField(max_length=100, null=True, blank=True)
    civil_construction_phase = models.CharField(max_length=100, null=True, blank=True)
    electric_equipment_installation = models.CharField(max_length=100, null=True, blank=True)
    electricity_generated = models.CharField(max_length=100, null=True, blank=True)
    ppa_details = models.CharField(max_length=100, null=True, blank=True)
    date_of_operation = models.CharField(max_length=100)
    image = models.CharField(max_length=100)
    other_properties = JSONField(null=True, blank=True)
    hydro_summary = models.TextField(null=True, blank=True)

    class Meta:
        ordering = ['name']

    def __str__(self):
        return self.name

    @property
    def value(self):
        return self.hydropower.count()

    @property
    def issue_date(self):
        return "{}/{}/{}".format(self.issue_date_months, self.issue_date_days, self.issue_date_years)

    @property
    def validity_date(self):
        return "{}/{}/{}".format(self.validity_date_months, self.validity_date_days, self.validity_date_years)

    @property
    def latitude(self):
        return self.latlong.y if self.latlong else 0

    @property    
    def longitude(self):
        return self.latlong.x if self.latlong else 0

def validate_file_extension(value):
    if not value.name.endswith('.geojson'):
        raise ValidationError('Error message')

class HazardType(models.Model):
    title = models.CharField(max_length=50, null=True, blank=True)
    about = models.CharField(max_length=500, null=True, blank=True)

    def __str__(self):
        return self.title

class HazardLayer(models.Model):
    hazard_type = models.ForeignKey(HazardType, on_delete=models.CASCADE, related_name='HazardLayer', null=True, blank=True)
    title = models.CharField(max_length=50, null=True, blank=True)
    about = models.CharField(max_length=500, null=True, blank=True)
        
    def __str__(self):
        return self.title

class HazardSubLayer(models.Model):
    hazard_layer = models.ForeignKey(HazardLayer, on_delete=models.CASCADE, related_name='HazardSubLayer')
    hazard_subLayer = models.CharField(max_length=50, null=True, blank=True)
    workspace = models.CharField(max_length=50, null=True, blank=True)
    layername=models.CharField(max_length=50, null=True, blank=True)
    center = models.CharField(max_length=100, null=True, blank=True)

    def __str__(self):
        return "{}-{}".format(self.hazard_layer,self.hazard_subLayer)

# class HazardSubLayerDetail(models.Model):
#     hazard_subLayer = models.ForeignKey(HazardSubLayer, on_delete=models.CASCADE,related_name='HazardSubLayerDetail')
#     returnperiod = models.CharField(max_length=50, null=True, blank=True)
#     workspace = models.CharField(max_length=50, null=True, blank=True)
#     layername=models.CharField(max_length=50, null=True, blank=True)
#     center = models.CharField(max_length=100, null=True, blank=True)

#     def __str__(self):
#         return self.layername

class ExposureType(models.Model):
    title = models.CharField(max_length=50, null=True, blank=True)
    about = models.CharField(max_length=500, null=True, blank=True)

    def __str__(self):
        return self.title


class ExposureLayer(models.Model):
    exposure_type = models.ForeignKey(ExposureType, on_delete=models.CASCADE, related_name='ExposureLayer', null=True, blank=True)
    title = models.CharField(max_length=50, null=True, blank=True)
    about = models.CharField(max_length=500, null=True, blank=True)
        
    def __str__(self):
        return "{}-{}".format(self.exposure_type,self.title)



class ExposureLayerDetail(models.Model):
    exposure_subLayer = models.ForeignKey(ExposureLayer, on_delete=models.CASCADE,related_name='ExposureLayerDetail')
    title = models.CharField(max_length=50, null=True, blank=True)
    workspace = models.CharField(max_length=50, null=True, blank=True)
    layername=models.CharField(max_length=50, null=True, blank=True)
    center = models.CharField(max_length=100, null=True, blank=True)

    def __str__(self):
        return "{}-{}".format(self.exposure_subLayer.exposure_type.title,self.exposure_subLayer.title)

# end publish data model
