from django.db import models
from django.conf import settings

class Basket(models.Model):
    user = models.ForeignKey(settings.AUTH_USER_MODEL, null=True, blank=True)
    billing_address = models.ForeignKey('a.Address', related_name='basket_billing_receiver', blank=True, null=True)

class CreditCheck(models.Model):
    user = models.ForeignKey(settings.AUTH_USER_MODEL, blank=True, null=True)

