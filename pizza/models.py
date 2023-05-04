from django.db import models

# Create your models here.

class PizzaType(models.Model):
    name = models.CharField(max_length=255)

class Pizza(models.Model):
    name = models.CharField(max_length=255)
    descriptions = models.CharField(max_length=255, blank=True)
    type = models.ForeignKey(PizzaType, on_delete=models.CASCADE)
    price = models.FloatField()

class PizzaImage(models.Model):
    image = models.CharField(max_length=999)
    pizza = models.ForeignKey(Pizza, on_delete=models.CASCADE)