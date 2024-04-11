from django.db import models


class Person(models.Model):
    name = models.ForeignKey('PersonName', on_delete=models.CASCADE)
    surname = models.ForeignKey('PersonSurname', on_delete=models.CASCADE)
    patronymic = models.ForeignKey('PersonPatronymic', on_delete=models.CASCADE)


class PersonName(models.Model):
    name = models.CharField(max_length=130, unique=True, null=False, blank=False)


class PersonSurname(models.Model):
    surname = models.CharField(max_length=130, unique=True, null=False, blank=False)


class PersonPatronymic(models.Model):
    patronymic = models.CharField(max_length=130, unique=True, null=False, blank=False)
