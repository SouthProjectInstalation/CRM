from django.db import models

from phonenumber_field.modelfields import PhoneNumberField


class Email(models.Model):
    email = models.EmailField(unique=True)

    def __str__(self):
        return f'{self.email}'


class Phone(models.Model):
    number = PhoneNumberField(unique=True, blank=False)

    def __str__(self):
        return f'{self.number}'


class Social(models.Model):
    url = models.URLField(unique=True)

    def __str__(self):
        return f'{self.url}'
