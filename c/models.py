from django.contrib.auth.models import AbstractUser
from django.db import models

class User(AbstractUser):
    credit_check = models.ForeignKey('b.CreditCheck',
        blank=True, null=True, related_name='delta_vista_check_initial'
    )

