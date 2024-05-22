from django.shortcuts import render
from .serializers import UserSerializer, ChefSerializer
from .models import User, CustomUser, Chef
from rest_framework.viewsets import ModelViewSet
from rest_framework.response import Response
from rest_framework import status
# Create your views here.

class CreateUser(ModelViewSet):
    queryset = CustomUser.objects.all()
    serializer_class = UserSerializer
  

class CreateChef(ModelViewSet):
    queryset = Chef.objects.all()
    serializer_class = ChefSerializer
