from rest_framework import serializers
from petter.models import User, Profile, Pets
#import Pet model when DB created

class ProfileSerializer(serializers.ModelSerializer):
    class Meta:
        model = Profile
        fields = '__all__'

class UserSerializer(serializers.ModelSerializer):
    class Meta:
        model = User
        exclude = ['password']

class PetsSerializer(serializers.ModelSerializer):
    class Meta:
        model = Pets
        fields = ('name', 'adoption_fee', 'breeds_display', 'coat', 'contact_number', 'created_at', 'age', 
                 'status', 'desexed', 'gender', 'group', 'heart_worm_treated', 'medical_notes', 'personality', 
                 'senior', 'size', 'photos', 'state', 'vaccinate', 'wormed', 'postcode', 'postcode_range'
        )