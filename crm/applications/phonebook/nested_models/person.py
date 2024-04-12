from django.db import models


class Person(models.Model):
    surname = models.ForeignKey('PersonSurname', on_delete=models.CASCADE, verbose_name='Фамилия')
    name = models.ForeignKey('PersonName', on_delete=models.CASCADE, verbose_name='Имя')
    patronymic = models.ForeignKey('PersonPatronymic', on_delete=models.CASCADE, verbose_name='Отчество')

    class Meta:
        verbose_name = 'Физическое лицо'
        verbose_name_plural = 'Физические лица'
        ordering = ['surname', 'name', 'patronymic']


class PersonSurname(models.Model):
    surname = models.CharField(max_length=130, unique=True, null=False, blank=False, verbose_name='Фамилия')

    class Meta:
        verbose_name = 'Фамилия физического лица'
        verbose_name_plural = 'Фамилии физических лиц'
        ordering = ['surname']


class PersonName(models.Model):
    name = models.CharField(max_length=130, unique=True, null=False, blank=False, verbose_name='Имя')

    class Meta:
        verbose_name = 'Имя физического лица'
        verbose_name_plural = 'Имена физических лиц'
        ordering = ['name']


class PersonPatronymic(models.Model):
    patronymic = models.CharField(max_length=130, unique=True, null=False, blank=False, verbose_name='Фамилия')

    class Meta:
        verbose_name = 'Отчество физического лица'
        verbose_name_plural = 'Отчества физических лиц'
        ordering = ['patronymic']
