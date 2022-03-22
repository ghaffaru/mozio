from rest_framework import serializers
# from
from rest_framework_gis.serializers import  GeoModelSerializer

from . import models


class ProviderSerializer(serializers.ModelSerializer):
    class Meta:
        fields = '__all__'
        model = models.Provider
        read_only_fields = ('createdAt',)


class ProviderNameSerializer(serializers.ModelSerializer):
    class Meta:
        fields = ('name',)
        model = models.Provider


class PolygonSerializer(GeoModelSerializer):

    class Meta:
        fields = ('id','name','price', 'geo', 'provider')
        model = models.Polygon
        read_only_fields = ('createdAt',)
        geo_field = 'geo'
        depth = 1


class CreatePolygonSerializer(serializers.Serializer):
    name = serializers.CharField(required=True)
    price = serializers.DecimalField(required=True, max_digits=50, decimal_places=2)
    latitude = serializers.DecimalField(required=True, max_digits=5, decimal_places=2)
    longitude = serializers.DecimalField(required=True, max_digits=5, decimal_places=2)
    provider = serializers.IntegerField(required=True)
