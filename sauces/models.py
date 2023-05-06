from django.db import models

# Create your models here.
class Sauce(models.Model):
    name = models.CharField(max_length=255)
    price = models.FloatField()

class SauceImage(models.Model):
    image = models.CharField(max_length=999)
    sauce = models.ForeignKey(Sauce, on_delete=models.CASCADE)


