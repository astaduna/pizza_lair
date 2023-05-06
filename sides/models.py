from django.db import models

# Create your models here.
class Side(models.Model):
    name = models.CharField(max_length=255)
    description = models.CharField(max_length=255, blank=True)
    price = models.FloatField()
    allergens = models.CharField(max_length=255, blank=True)

class SideImage(models.Model):
    image = models.CharField(max_length=999)
    side = models.ForeignKey(Side, on_delete=models.CASCADE)