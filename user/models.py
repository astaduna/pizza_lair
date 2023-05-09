from django.db import models
from django.contrib.auth.models import User

# Create your models here.
class Profile(models.Model):
    user = models.OneToOneField(User, on_delete=models.CASCADE, default=User.objects.first())
    name = models.CharField(max_length=255, blank=True)
    address = models.CharField(max_length=255, blank=True)
    house_number = models.IntegerField(5)
    city = models.CharField(max_length=255, blank=True)
    country = models.CharField(max_length=255, blank=True)
    zip = models.IntegerField()
    profile_image = models.CharField(max_length=9999, blank=True)
