from django.db import models

class APackage(models.Model):
    delivery_person = models.ForeignKey('a.Person')

class DeliveryCountry(models.Model):
    name = models.CharField(max_length=80)
