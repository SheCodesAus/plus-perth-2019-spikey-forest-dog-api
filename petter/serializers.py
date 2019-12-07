from rest_framework import serializers
from petter.models import User, Profile, Pets
from django.db import transaction
from .models import Profile
from .helpers import send_password_reset_email

class ProfileSerializer(serializers.ModelSerializer):
    class Meta:
        model = Profile
        fields = '__all__'

class UserProfileSerializer(serializers.ModelSerializer):
    class Meta:
        model = Profile
        exclude = ["user"]

class UserSerializer(serializers.ModelSerializer):
    profile = UserProfileSerializer(many=False, required=False)
    class Meta:
        model = User
        fields = ['id', 'username', 'is_active', 'email', 'first_name', 'last_name','profile']

    @transaction.atomic
    def create(self, validated_data):
        # remove the profile data
        profile_data = validated_data.pop("profile",None)
        # create user from validated data
        user = User(**validated_data)

        # set user password to blank
        user.set_unusable_password()

        # if you wanted to set the password you could use these lines
        # user.set_password(validated_data.get('password'))
        # user.is_active = False

        # save the user
        user.save()
        # update the user profile
        if profile_data:
            Profile.objects.filter(user=user).update(**profile_data)

        # send user password setup email
        send_password_reset_email(user)
        return user

    def update(self, instance, validated_data):
        # remove the profile data
        profile_data = validated_data.pop("profile",None)
        # run the normal update process
        super().update(instance, validated_data)
        # handle extra profile information
        if profile_data:
            Profile.objects.filter(user=instance).update(**profile_data)
        return instance

class PasswordSerializer(serializers.Serializer):
    """
    Serializer for password change endpoint.
    """

    new_password = serializers.CharField(required=True)

class PetsSerializer(serializers.ModelSerializer):
    class Meta:
        model = Pets
        fields = ('name', 'adoption_fee', 'pet_type', 'breeds_display', 'contact_number', 'created_at', 'age', 
                 'status', 'desexed', 'gender', 'medical_notes', 'personality', 
                 'senior', 'size', 'photos', 'state', 'vaccinate', 'wormed', 'postcode'
        )

