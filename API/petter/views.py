from django.shortcuts import render, redirect
from petter.models import User, Profile
from petter.serializers import ProfileSerializer, UserSerializer
from rest_framework import generics, viewsets
from django.contrib.auth import login, authenticate
from django.contrib.auth.forms import UserCreationForm
from rest_framework.permissions import IsAuthenticated

# Create your views here.

class ProfileViewSet(viewsets.ModelViewSet):
    queryset = Profile.objects.all()
    serializer_class = ProfileSerializer
    permission_classes = (IsAuthenticated,)

class UserViewSet(viewsets.ModelViewSet):
    queryset = User.objects.all()
    serializer_class = UserSerializer
    permission_classes = (IsAuthenticated,)

# class RegisterViewSet(viewsets.ModelViewSet):
#     form = Profile(request.POST)
    

