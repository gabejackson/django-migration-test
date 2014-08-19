from django.db import models

class Person(models.Model):
    name = models.CharField(max_length=60)

class Address(models.Model):
    country = models.ForeignKey('c.DeliveryCountry')
