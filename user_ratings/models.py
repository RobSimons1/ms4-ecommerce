from django.db import models
from products.models import Product # Imported for product specific review
from django.utils import timezone

# Create your models here.

class Review(models.Model):
    product = models.ForeignKey(
        Product, on_delete=models.SET_NULL, null=True, blank=True)
    name = models.CharField(max_length=200, blank=False, default='')
    review = models.CharField(max_length=1000, blank=False, default='')
    RATING_CHOICES = (
        ("1", '1'),
        ("2", '2'),
        ("3", '3'),
        ("4", '4'),
        ("5", '5'),
    )
    rating = models.CharField(max_length=10,
                                      choices=RATING_CHOICES,
                                      default="3")
    date = models.DateTimeField(default=timezone.now, blank=True)

    def __str__(self):
        return self.name
