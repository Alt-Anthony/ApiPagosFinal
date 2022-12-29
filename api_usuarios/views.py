from django.shortcuts import render
from rest_framework import generics
from .serializers import UserSerializer
from django.contrib.auth.models import User
from django.shortcuts import get_object_or_404
from rest_framework.decorators import api_view
from django.contrib.auth import get_user_model

class UserCreateView(generics.CreateAPIView):
    serializer_class = UserSerializer
    
class UserListView(generics.ListAPIView):
    queryset = User.objects.all()
    serializer_class = UserSerializer


@api_view(['GET'])
def get_user(request, username):
    User = get_user_model()
    User = get_object_or_404(User, username=username)