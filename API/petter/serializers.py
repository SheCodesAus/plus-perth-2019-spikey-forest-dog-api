from rest_framework import serializers
from petter.models import User, Profile
#import Pet model when DB created

class ProfileSerializer(serializers.ModelSerializer):
    class Meta:
        model = Profile
        fields = '__all__'

class UserSerializer(serializers.ModelSerializer):
    profile = ProfileSerializer(many=False, required=False)
    class Meta:
        model = User
        fields = ['id', 'url', 'username', 'is_active', 'email', 'first_name', 'last_name','profile']