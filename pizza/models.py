from django.db import models
from product.models import Product


# Create your models here.
class PizzaType(models.Model):
    name = models.CharField(max_length=255, blank=True)

class Pizza(models.Model):
    toppings = models.CharField(max_length=255, blank=True)
    descriptions = models.CharField(max_length=999, blank=True)
    type = models.ForeignKey(PizzaType, on_delete=models.CASCADE)
    allergens = models.CharField(max_length=255, blank=True)
    product = models.OneToOneField(Product, on_delete=models.CASCADE)

class PizzaImage(models.Model):
    image = models.CharField(max_length=999)
    pizza = models.ForeignKey(Pizza, on_delete=models.CASCADE)