from django.db import models

class Profile(models.Model):
    user = models.OneToOneField(User, on_delete=models.CASCADE, primary_key=True)
    username = models.CharField(max_length=50)
    first_name = models.CharField(max_length=50)
    email = models.Charfield(max_length=100)
    postcode = models.CharField(max_length=4)
