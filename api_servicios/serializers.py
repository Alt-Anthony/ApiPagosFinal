from rest_framework import serializers
from .models import Service

class ServiceSerializer(serializers.Serializer):
    class Meta:
        model = Service
        fields = '__all__'
    