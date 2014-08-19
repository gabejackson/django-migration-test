from django.db import models

class Address(models.Model):
    country = models.ForeignKey('c.DeliveryCountry')

class Person(models.Model):
    name = models.CharField(max_length=60)