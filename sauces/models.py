from django.db import models
from product.models import Product

# Create your models here.
class Sauce(models.Model):
    product = models.OneToOneField(Product, on_delete=models.CASCADE)


class SauceImage(models.Model):
    image = models.CharField(max_length=999)
    sauce = models.ForeignKey(Sauce, on_delete=models.CASCADE)


