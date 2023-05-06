from django.db import models

# Create your models here.
class User(models.Model):
    name = models.CharField(max_length=255)
    address = models.CharField(max_length=255)
    house_number = models.IntegerField(5)
    city = models.CharField(max_length=255)
    country = models.CharField(max_length=255)
    zip = models.IntegerField(10)
