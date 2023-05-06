from django.db import models
from user.models import User
from django.utils import timezone
from product.models import Product
from offers.models import Offer

# Create your models here.

class OrderPayment(models.Model):
    user = models.ForeignKey(User, on_delete=models.CASCADE)
    timestamp = models.DateTimeField(default=timezone.now, editable=False)

class Order(models.Model):
    user = models.ForeignKey(User, on_delete=models.CASCADE)
    in_cart = models.BooleanField(default=True, blank=True)
    payment = models.ForeignKey(OrderPayment, on_delete=models.CASCADE)


class OrderItem(models.Model):
    order = models.ForeignKey(Order, on_delete=models.CASCADE)
    quantity = models.PositiveIntegerField()
    product = models.ForeignKey(Product, on_delete=models.CASCADE)
    offer = models.ForeignKey(Offer, on_delete=models.CASCADE)

