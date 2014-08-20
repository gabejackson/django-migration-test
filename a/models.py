from django.db import models
from django.conf import settings

class Address(models.Model):
    country = models.ForeignKey('d.DeliveryCountry')

class ShopUserAddress(models.Model):
    user = models.ForeignKey(settings.AUTH_USER_MODEL, related_name='addresses')