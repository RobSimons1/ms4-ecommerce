from django.db import models
from django.contrib.auth.models import User
from django.db.models.signals import post_save
from django.dispatch import receiver
from datetime import datetime

# Create your models here.

class UserProfile(models.Model):
    """ A User profile model for maintaining 
    delivery information and order history """

    user = models.OneToOneField(User, on_delete=models.CASCADE)
    full_name = models.CharField(max_length=50, blank=True)
    default_phone_number = models.CharField(max_length=20, blank=True)
    default_country = models.CharField(max_length=40, blank=True)
    default_postcode = models.CharField(max_length=20, blank=True)
    default_town_or_city = models.CharField(max_length=40, blank=True)
    default_street_address1 = models.CharField(max_length=40, blank=True)
    default_street_address2 = models.CharField(max_length=40, blank=True)
    default_county = models.CharField(max_length=40, blank=True)
    date = models.DateTimeField(default=datetime.now, blank=True)

    def __str__(self):
        return "{0}-{1}-{2}".format(self.id, self.date, self.full_name)

@receiver(post_save, sender=User)
def create_or_update_user_profile(sender, instance, created, **kwargs):
    """
    Create a user profile for all new users
    """
    if created:
        UserProfile.objects.create(user=instance)
    # Existing users: just save the profile
    instance.userprofile.save()
