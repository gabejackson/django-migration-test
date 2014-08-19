from django.db import models

class Country(models.Model):
    name = models.CharField('Country name', max_length=80)