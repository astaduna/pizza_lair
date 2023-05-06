from django.db import models
from pizza.models import Pizza
from sides.models import Side
from sauces.models import Sauce
from drinks.models import Drink

# Create your models here.
class Product(models.Model):
    name = models.CharField(max_length=255)
    price = models.IntegerField()
    pizzas = models.ManyToManyField(Pizza, related_name='offers_pizzas', blank=True)
    sides = models.ManyToManyField(Side, related_name='offers_sides', blank=True)
    drinks = models.ManyToManyField(Drink, related_name='offers_drinks', blank=True)
    sauce = models.ManyToManyField(Sauce, related_name='offers_drinks', blank=True)