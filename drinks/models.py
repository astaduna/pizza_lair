from django.db import models

# Create your models here.
class Drink(models.Model):
    name = models.CharField(max_length=255)
    price = models.IntegerField()

class DrinkImage(models.Model):
    image = models.CharField(max_length=999)
    drink = models.ForeignKey(Drink, on_delete=models.CASCADE)