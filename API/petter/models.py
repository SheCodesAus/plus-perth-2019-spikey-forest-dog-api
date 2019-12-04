from django.db import models
from django.contrib.auth import get_user_model


User = get_user_model()

class Profile(models.Model):
    user = models.OneToOneField(User, on_delete=models.CASCADE, primary_key=True)
    # username = models.CharField(max_length=50)
    # first_name = models.CharField(max_length=50)
    email = models.CharField(max_length=100)
    postcode = models.CharField(max_length=4)

    def __str__(self):
        return self.name

class Pets(models.Model):
    name = models.CharField (max_length=50)
    adoption_fee = models.CharField(max_length=50)
    breeds_display = models.CharField(max_length=50)
    coat = models.CharField(max_length=50)
    contact_number = models.CharField(max_length=50)
    created_at = models.CharField(max_length=50)
    age = models.CharField(max_length=2)
    status = models.CharField(max_length=50)
    desexed = models.CharField(max_length=50)
    gender = models.CharField(max_length=50)
    group = models.CharField(max_length=50)
    heart_worm_treated = models.CharField(max_length=50)
    medical_notes = models.CharField(max_length=50)
    personality = models.CharField(max_length=250)
    senior = models.CharField(max_length=50)comm
    size = models.CharField(max_length=50)
    photos = models.CharField(max_length=50)
    state = models.CharField(max_length=50)
    vaccinate = models.CharField(max_length=50)
    wormed = models.CharField(max_length=50)
    postcode = models.CharField(max_length=4)
    postcode_range = models.CharField(max_length=50)

    def __str__(self):
        return self.name