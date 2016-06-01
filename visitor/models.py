from __future__ import unicode_literals

from django.db import models
from django.core.validators import EmailValidator
from phonenumber_field.modelfields import PhoneNumberField
# visitor data model


class Visitor(models.Model):
    name = models.CharField(max_length=60)
    email = models.CharField(max_length=225, validators=[EmailValidator])
    photo = models.ImageField(blank=True)
    phone_number = PhoneNumberField(blank=False)
    company_name = models.CharField(max_length=60, blank=True, default='')
    company_to_visit = models.CharField(max_length=60, blank=True, default='')
    employee_to_visit = models.CharField(max_length=60, blank=True, default='')
    subscribe_to_mailing_list = models.BooleanField(default=False)

    def __str__(self):
        return self.name
