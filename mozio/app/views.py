from rest_framework import generics, views
from rest_framework.response import Response

from django.contrib.gis.geos import Point
from . import models, serializers
from django.shortcuts import get_object_or_404


class ProviderListCreateView(generics.ListCreateAPIView):
    queryset = models.Provider.objects.order_by('-createdAt')
    serializer_class = serializers.ProviderSerializer


class ProviderRetrieveUpdateDeleteView(generics.RetrieveUpdateDestroyAPIView):
    serializer_class = serializers.ProviderSerializer
    queryset = models.Provider.objects.all()
    lookup_field = 'id'


class PolygonListCreateView(generics.ListCreateAPIView):
    queryset = models.Polygon.objects.order_by('createdAt')
    serializer_class = serializers.PolygonSerializer

    def create(self, request, *args, **kwargs):
        serializer = serializers.CreatePolygonSerializer(data=request.data)

        if serializer.is_valid():

            provider = get_object_or_404(models.Provider, pk=serializer.validated_data['provider'])

            polygon = models.Polygon.objects.create(name=serializer.validated_data['name'],
                                                    price=serializer.validated_data['price'],
                                                    geo=Point(float(serializer.validated_data['latitude']),
                                                              float(serializer.validated_data['longitude'])),
                                                    provider=provider)

            return Response(status=201, data=serializers.PolygonSerializer(polygon).data)
        else:
            return Response(status=400, data=serializer.errors)


class PolygonRetrieveUpdateDeleteView(generics.RetrieveUpdateDestroyAPIView):
    serializer_class = serializers.PolygonSerializer
    queryset = models.Polygon.objects.all()
    lookup_field = 'id'

    def update(self, request, *args, **kwargs):

        serializer = serializers.CreatePolygonSerializer(data=request.data)

        if serializer.is_valid():

            provider = get_object_or_404(models.Provider, pk=serializer.validated_data['provider'])

            polygon = get_object_or_404(models.Polygon, pk=kwargs.get('id'))
            polygon.name = serializer.validated_data['name']
            polygon.price = serializer.validated_data['price']
            polygon.geo = Point(float(serializer.validated_data['latitude']),
                                float(serializer.validated_data['longitude']))
            polygon.provider = provider

            polygon.save()

            return Response(status=201, data=serializers.PolygonSerializer(polygon).data)
        else:
            return Response(status=400, data=serializer.errors)


class FilterPolygonsView(views.APIView):
    def get(self, request, lat, long):
        point = Point(float(lat), float(long))

        polygons = models.Polygon.objects.filter(geo=point)

        return Response(status=200, data={'polygons': serializers.PolygonSerializer(polygons, many=True).data})


# get polygons for a particular provider
class PolygonsForProviderView(views.APIView):
    def get(self, request, provider_id):
        provider = get_object_or_404(models.Provider, pk=provider_id)

        polygons = models.Polygon.objects.filter(provider=provider)

        return Response(status=200, data=serializers.PolygonSerializer(polygons, many=True).data)
