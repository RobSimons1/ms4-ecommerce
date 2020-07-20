from django.db import models

# Create your models here.

class Item(models.Model):
    
    name = models.CharField(max_length=200, blank=False)
    beer = models.CharField(max_length=500, default='', blank=False)
    review = models.CharField(max_length=2000, default='', blank=False)
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

    def __str__(self):
        return self.name