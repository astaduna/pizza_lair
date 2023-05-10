from django.db import models
from product.models import Product

# Create your models here.
class Drink(models.Model):
    product = models.OneToOneField(Product, on_delete=models.CASCADE)

class DrinkImage(models.Model):
    image = models.CharField(max_length=999)
    drink = models.ForeignKey(Drink, on_delete=models.CASCADE)