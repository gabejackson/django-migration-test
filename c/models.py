from django.db import models

class DeliveryCountry(models.Model):
    country = models.ForeignKey('b.Country')

class BeyelerPackage(models.Model):
    delivery_person = models.ForeignKey('a.Person')
