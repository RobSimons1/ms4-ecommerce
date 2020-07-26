from django.db import models
from products.models import Product # Imported for product specific review
from django.utils import timezone

# Create your models here.

class Item(models.Model):
    name = models.CharField(max_length=200, blank=False, default='')
    beer = models.CharField(max_length=500, default='', blank=False)
    review = models.TextField(max_length=2000, default='', blank=False)
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
    done = models.BooleanField(blank=False, default=False)
    date = models.DateTimeField(default=timezone.now, blank=True)

    def __str__(self):
        return self.name

class ReviewLineItem(models.Model):
    """ Model to add specific review to specific product item """
    # product = models.OneToOneField(Product, on_delete=models.CASCADE, primary_key=True, default="")
    product = models.ForeignKey(Product, null=False, default='')
    #new_item = models.ForeignKey(ItemForm, null=False, default='') # Added to try and get new_item 
    item = models.ForeignKey(Item, null=False, default='') # Added to try and get item 

    def __str__(self):
        return "{0} {1}".format(
            self.product.name, self.item.name)     