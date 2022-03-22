from django.db import models
from django.contrib.gis.db.models import PointField


class Provider(models.Model):
    name = models.CharField(max_length=255)
    email = models.CharField(max_length=255, unique=True)
    phoneNumber = models.CharField(max_length=255, unique=True)
    language = models.CharField(max_length=100)
    currency = models.CharField(max_length=4)
    createdAt = models.DateTimeField(auto_now_add=True)


class Polygon(models.Model):
    provider = models.ForeignKey(Provider, on_delete=models.CASCADE)
    name = models.CharField(max_length=255)
    price = models.DecimalField(max_digits=100, decimal_places=2)
    geo = PointField()
    createdAt = models.DateTimeField(auto_now_add=True)

    # @property
    # def lat(self):
    #     return self.geo.po