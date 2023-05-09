from django.db import models
from product.models import Product

# Create your models here.

class Cart(models.Model):
    product = models.ForeignKey(Product, on_delete=models.CASCADE)
    quantity = models.PositiveIntegerField()
    price = models.IntegerField(default=0)


def __str__(self):
    return f'{self.product.name} - {self.quantity} x {self.price}'