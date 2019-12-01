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
