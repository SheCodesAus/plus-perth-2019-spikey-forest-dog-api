from rest_framework import serializers
from django.shortcuts import render, redirect
from petter.models import User, Profile, Pets
from petter.serializers import ProfileSerializer, UserSerializer, PetsSerializer
from django.http import HttpResponse
from .forms import SignupForm
from rest_framework import generics, viewsets
from django.contrib.auth import login, authenticate
from django.contrib.auth.forms import UserCreationForm
from rest_framework.permissions import IsAuthenticated
from django.contrib.sites.shortcuts import get_current_site
from django.utils.encoding import force_bytes, force_text
from django.utils.http import urlsafe_base64_encode, urlsafe_base64_decode
from django.template.loader import render_to_string
from .tokens import account_activation_token
from django.contrib.auth.models import User
from django.core.mail import EmailMessage


# Create your views here.

PET_LISTING_URL = "http://www.petrescue.com.au/api/listings"


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
    
class PetsViewSet(viewsets.ModelViewSet):
    queryset = Pets.objects.all()
    serializer_class = PetsSerializer

def import_data(request):
    with urlopen(PET_LISTING_URL)  as fp:
        pets_listings = {
            "name": item.name.string,
            "adoption_fee": item.adoption_fee.string,
            "breeds_display": item.breeds_display.string,
            "coat": item.coat.string,
            "contact_number": item.contact_number.string,
            "created_at": item.created_at.string,
            "age": item.age.string,
            "status": item.status.string,
            "desexed": item.desexed.string,
            "gender": item.gender.string,
            "group": item.group.string,
            "heart_worm_treated": item.heart_worm_treated.string,
            "medical_notes": item.medical_notes.string,
            "personality": item.personality.string,
            "senior": item.senior.string,
            "size": item.size.string,
            "photos": item.photos.string,
            "state": item.state.string,
            "vaccinate": item.vaccinate.string,
            "wormed": item.wormed.string,
            "postcode": item.postcode.string,
            "postcode_range": item.postcode_range.string,
        }
