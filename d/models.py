from django.db import models

class DeliveryCountry(models.Model):
    name = models.CharField(max_length=80)

class BeyelerPackage(models.Model):
    delivery_address = models.ForeignKey('a.ShopUserAddress')