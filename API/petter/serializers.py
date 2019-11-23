from rest_framework import serializers
from petter.models import User, Profile
#import Pet model when DB created

class ProfileSerializer(serializers.ModelSerializer):
    class Meta:
        model = Profile
        fields = '__all__'

class UserSerializer(serializers.ModelSerializer):
    class Meta:
        model = User
        exclude = ['password']

# class PetSerializer(serializers.ModelSerializer):
#     class Meta:
#         model = Pet
#         fields = ''