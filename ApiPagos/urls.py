"""ApiPagos URL Configuration

The `urlpatterns` list routes URLs to views. For more information please see:
    https://docs.djangoproject.com/en/4.1/topics/http/urls/
Examples:
Function views
    1. Add an import:  from my_app import views
    2. Add a URL to urlpatterns:  path('', views.home, name='home')
Class-based views
    1. Add an import:  from other_app.views import Home
    2. Add a URL to urlpatterns:  path('', Home.as_view(), name='home')
Including another URLconf
    1. Import the include() function: from django.urls import include, path
    2. Add a URL to urlpatterns:  path('blog/', include('blog.urls'))
"""
from django.contrib import admin
from django.urls import path

from rest_framework import routers
from api_pagos.views import PaymentExpiredView, PaymentView 
from api_servicios.views import ServiceRest
from api_usuarios.views import UserCreateView, UserListView

from django.urls import re_path
from rest_framework import permissions
from drf_yasg.views import get_schema_view
from drf_yasg import openapi

from rest_framework_simplejwt.views import TokenObtainPairView, TokenRefreshView
schema_view = get_schema_view(
    openapi.Info(
        title="Api de Pagos",
        default_version='v1',
        description="Proyecto de Api para hacer pagos",
        terms_of_service="https://github.com/Alt-Anthony",
        contact=openapi.Contact(email="magusslather@gmail.com"),
        license=openapi.License(name="BSD License")
    ),
    public= True,
    permission_classes=[permissions.AllowAny],
)

router = routers.DefaultRouter()
router.register(r'service', ServiceRest, 'Service')
router.register(r'payment', PaymentView, 'Payment')
router.register(r'payment-expired', PaymentExpiredView, 'Payment-expired')


urlpatterns = [
    path('admin/', admin.site.urls),
    path('users', UserListView.as_view(), name='user-list'),
    path('user/create/', UserCreateView.as_view() ,name='user-create' ),
    
    re_path(r'^swagger(?P<format>\.json|\.yaml)$', schema_view.without_ui(cache_timeout=0), name="schema-json"),
    re_path(r'^swagger/$', schema_view.with_ui('swagger', cache_timeout=0), name="schema-swagger-ui"),
    re_path(r'^swagger/$', schema_view.with_ui('redoc',cache_timeout=0), name="schema-redoc"),

    path("token/", TokenObtainPairView.as_view(), name="get-token"),
    path("token/refresh/", TokenRefreshView.as_view(),name="refresh-token"),
    
]


urlpatterns += router.urls