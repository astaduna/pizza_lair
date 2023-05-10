from django.db import models
from product.models import Product

# Create your models here.
class Side(models.Model):
    product = models.OneToOneField(Product, on_delete=models.CASCADE)
    description = models.CharField(max_length=255, blank=True)
    allergens = models.CharField(max_length=255, blank=True)

class SideImage(models.Model):
    image = models.CharField(max_length=999)
    side = models.ForeignKey(Side, on_delete=models.CASCADE)