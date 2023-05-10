from django.db import models

# Create your models here.
class PizzaType(models.Model):
    name = models.CharField(max_length=255, blank=True)

class Pizza(models.Model):
    name = models.CharField(max_length=255)
    toppings = models.CharField(max_length=255, blank=True)
    descriptions = models.CharField(max_length=255, blank=True)
    type = models.ForeignKey(PizzaType, on_delete=models.CASCADE)
    price = models.IntegerField(default=True)
    allergens = models.CharField(max_length=255, blank=True)

class PizzaImage(models.Model):
    image = models.CharField(max_length=999)
    pizza = models.ForeignKey(Pizza, on_delete=models.CASCADE)