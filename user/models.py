from django.db import models
from django.contrib.auth.models import User

# Create your models here.
class Profile(models.Model):
    DEFAULT_PROFILE_IMAGE = '/images/profile.png'
    user = models.OneToOneField(User, on_delete=models.CASCADE)
    name = models.CharField(max_length=255)
    address = models.CharField(max_length=255)
    house_number = models.IntegerField(5)
    city = models.CharField(max_length=255)
    country = models.CharField(max_length=255)
    zip = models.IntegerField()
    profile_image = models.CharField(max_length=9999, default=DEFAULT_PROFILE_IMAGE)
