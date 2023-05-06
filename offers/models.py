from django.db import models
from product.models import Product

# Create your models here.
class Offer(models.Model):
    name = models.CharField(max_length=255)
    description = models.CharField(max_length=255, blank=True)
    total = models.IntegerField(default=True)
    discount = models.DecimalField(max_digits=6, decimal_places=2, default=0.0)
    pizzas = models.ManyToManyField(Product, related_name='offers_pizzas', blank=True)
    sides = models.ManyToManyField(Product, related_name='offers_sides', blank=True)
    drinks = models.ManyToManyField(Product, related_name='offers_drinks', blank=True)


class OfferImage(models.Model):
    image = models.CharField(max_length=999)
    offer = models.ForeignKey(Offer, on_delete=models.CASCADE)