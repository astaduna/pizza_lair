from django.db import models
from product.models import Product

# Create your models here.
class Offer(models.Model):
    product = models.OneToOneField(Product, on_delete=models.CASCADE)
    description = models.CharField(max_length=999, blank=True)



class OfferImage(models.Model):
    image = models.CharField(max_length=999)
    offer = models.ForeignKey(Offer, on_delete=models.CASCADE)