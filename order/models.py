from django.db import models
from product.models import Product
from django.contrib.auth.models import User

# Create your models here.

class Order(models.Model):
    user = models.IntegerField(User, default=True)
    product = models.OneToOneField(Product, on_delete=models.CASCADE)
    quantity = models.PositiveIntegerField(default=1)
    timestamp = models.DateTimeField(auto_now_add=True)
    is_payed = models.BooleanField(default=False)
