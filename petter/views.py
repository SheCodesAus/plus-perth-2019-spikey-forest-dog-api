from rest_framework.response import Response
from rest_framework.permissions import IsAuthenticated, IsAdminUser
from django.contrib.auth.models import User
from rest_framework import generics, viewsets, status
from rest_framework.decorators import action
from .permissions import IsAdminOrSelf
from .serializers import ProfileSerializer, UserSerializer, PetsSerializer, PasswordSerializer
from .models import User, Profile, Pets
from .helpers import send_password_reset_email


# from rest_framework import serializers
# from django.shortcuts import render, redirect
# from django.http import HttpResponse
# from django.contrib.auth import login, authenticate
# from django.contrib.auth.forms import UserCreationForm
# from django.contrib.sites.shortcuts import get_current_site
# from django.utils.encoding import force_bytes, force_text
# from django.utils.http import urlsafe_base64_encode, urlsafe_base64_decode
# from django.template.loader import render_to_string
# from .tokens import account_activation_token
# from django.core.mail import EmailMessage


# Create your views here.

PET_LISTING_URL = "http://www.petrescue.com.au/api/listings"


class ProfileViewSet(viewsets.ModelViewSet):
    """
    API endpoint that allows users to be viewed or edited.
    """

    queryset = Profile.objects.all()
    serializer_class = ProfileSerializer
    permission_classes = (IsAuthenticated,)

class UserViewSet(viewsets.ModelViewSet):
    """
    API endpoint that allows users to be viewed or edited.
    """

    queryset = User.objects.none()
    serializer_class = UserSerializer
    # permission_classes = (IsAuthenticated, IsAdminUser)

    def get_queryset(self):
        # if the user is admin, return all the users
        if self.request.user.is_superuser:
            return User.objects.all().order_by("-date_joined")
        # if the user is logged in, return only the active user
        if self.request.user:
            return User.objects.filter(pk=self.request.user.pk)
        # if there is no user, return no results
        return User.objects.none()

    @action(methods=["post"], detail=True, permission_classes=[IsAdminOrSelf])
    def set_password(self, request, pk=None):
        """ set the user password """
        serializer = PasswordSerializer(data=request.data)
        user = self.get_object()

        if serializer.is_valid():
            user.set_password(serializer.data.get("new_password"))
            user.save()
            return Response({"status": "password set"}, status=status.HTTP_200_OK)

        return Response(serializer.errors, status=status.HTTP_400_BAD_REQUEST)

    @action(methods=["get"], detail=True, permission_classes=[IsAdminOrSelf])
    def reset_password(self, request, pk=None):
        """ set the user password """
        user = self.get_object()
        send_password_reset_email(user)

        return Response({"status": "password reset"}, status=status.HTTP_200_OK)
    
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
