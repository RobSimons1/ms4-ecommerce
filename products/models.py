from django.db import models

# Create your models here.
class Product(models.Model):
    name = models.CharField(max_length=254, default='')
    description = models.CharField(max_length=254, default='')
    info = models.CharField(max_length=500, default='')
    blurb = models.TextField(default='')
    size = models.CharField(max_length=254, default='')
    alcohol = models.CharField(max_length=254, default='')
    price = models.DecimalField(max_digits=6, decimal_places=2)
    image = models.ImageField(upload_to='images')

    def __str__(self):
        return self.name

        