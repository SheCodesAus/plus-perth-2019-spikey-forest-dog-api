from django.shortcuts import render, redirect
from petter.models import User, Profile
from petter.serializers import ProfileSerializer, UserSerializer
#import pet serializer when model set up
from rest_framework import generics, viewsets
from django.contrib.auth import login, authenticate
from django.contrib.auth.forms import UserCreationForm

# Create your views here.

class ProfileViewSet(viewsets.ModelViewSet):
    queryset = Profile.objects.all()
    serializer_class = ProfileSerializer

class UserViewSet(viewsets.ModelViewSet):
    queryset = User.objects.all()
    serializer_class = UserSerializer
    
# class PetViewSet(viewsets.ModelViewSet):
#     queryset = Pet.objects.all()
#     serializer_class = PetSerializer
