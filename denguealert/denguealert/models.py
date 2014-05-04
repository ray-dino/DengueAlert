from django.contrib.gis.db import models


class DengueCase(models.Model):
    patient_name = models.CharField(max_length=2048, null=True, blank=True)
    created_date = models.DateField(auto_now_add=True)
    onset_date = models.DateField()


class DengueCaseLocation(models.Model):
    dengue_case = models.ForeignKey('DengueCase')
    name = models.CharField(max_length=2048, null=True, blank=True)
    address = models.CharField(max_length=2048, null=True, blank=True)
    latitude = models.FloatField()
    longitude = models.FloatField()
    point = models.PointField()


class Baranggay(models.Model):
    name = models.CharField(max_length=2048, null=True, blank=True)
    municipality = models.ForeignKey('Municipality')
    area = models.MultiPolygonField()


class Municipality(models.Model):
    name = models.CharField(max_length=2048, null=True, blank=True)
    area = models.MultiPolygonField()
