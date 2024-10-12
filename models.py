from django.db import models
from django.contrib.gis.db import models 


class Clinics(models.Model):
    name = models.CharField(max_length=254)
    tessellate = models.BigIntegerField()
    visibility = models.BigIntegerField()
    geom = models.MultiPointField(srid=4326)  

    class Meta:
        verbose_name_plural = 'Clinics'

    def __str__(self):
        return self.name 
    
    
class Wards(models.Model):
    fid = models.IntegerField()
    objectid_1 = models.FloatField()
    admin3name = models.CharField(max_length=254)
    admin3pcod = models.CharField(max_length=254)
    admin2name = models.CharField(max_length=254)
    admin2pcod = models.CharField(max_length=254)
    admin1name = models.CharField(max_length=254)
    admin1pcod = models.CharField(max_length=254)
    shape_leng = models.FloatField()
    shape_area = models.FloatField()
    case_recor = models.CharField(max_length=255, null=True)
    num_of_cas = models.CharField(max_length=255, null=True)
    hotspot =  models.CharField(max_length=255, null=True)
    geom = models.MultiPolygonField(srid=4326)

    class Meta:
        verbose_name_plural = 'Wards'

    def __str__(self):
        return self.admin3name 
    
class Hospitals(models.Model):
    name = models.CharField(max_length=254)
    tessellate = models.BigIntegerField()
    visibility = models.BigIntegerField()
    geom = models.MultiPointField(srid=4326)

    class Meta:
        verbose_name_plural = 'Hospitals'

    def __str__(self):
        return self.name 
    
