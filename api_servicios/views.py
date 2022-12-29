from django.shortcuts import render

from rest_framework import viewsets
from .serializers import ServiceSerializer
from .models import Service

from rest_framework.permissions import AllowAny, IsAdminUser, IsAuthenticated

class ServiceRest(viewsets.ModelViewSet):
    queryset = Service.objects.all()
    serializer_class = ServiceSerializer
    #throttle_scope = 'all'
    def get_permissions(self):
        if self.request.method == 'GET':
            return [AllowAny()]
        return [AllowAny()]
