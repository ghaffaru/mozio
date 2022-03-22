from rest_framework import generics
from . import models, serializers


class ProviderListCreateView(generics.ListCreateAPIView):
    queryset = models.Provider.objects.order_by('-createdAt')
    serializer_class = serializers.ProviderSerializer


class ProviderRetrieveUpdateDeleteView(generics.RetrieveUpdateDestroyAPIView):
    serializer_class = serializers.ProviderSerializer
    queryset = models.Provider.objects.all()
    lookup_field = 'id'
