from django.contrib.gis.db import models


class DengueCase(models.Model):
    date = models.DateField(auto_now_add=True)
    address = models.CharField(max_length=2048, null=True, blank=True)
    latitude = models.FloatField()
    longitude = models.FloatField()
    point = models.PointField()