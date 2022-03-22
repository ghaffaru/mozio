from rest_framework import serializers
from . import models


class ProviderSerializer(serializers.ModelSerializer):
    class Meta:
        fields = '__all__'
        model = models.Provider
