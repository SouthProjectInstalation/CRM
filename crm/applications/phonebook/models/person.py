from django.db import models


class Person(models.Model):
    surname = models.ForeignKey(
        'Surname', on_delete=models.CASCADE, verbose_name='Фамилия'
    )
    name = models.ForeignKey(
        'Name', on_delete=models.CASCADE, verbose_name='Имя'
    )
    patronymic = models.ForeignKey(
        'Patronymic', null=True, blank=True, on_delete=models.CASCADE, verbose_name='Отчество'
    )

    def __str__(self):
        surname = self.surname.surname
        name = self.name.name
        patronymic = " " + self.patronymic.patronymic if self.patronymic else ''
        return f'{surname} {name}{patronymic}'

    class Meta:
        verbose_name = 'Физическое лицо'
        verbose_name_plural = 'Физические лица'
        # TODO Упорядочивание лучше использовать с помощью Proxy-моделей
        # ordering = ['surname', 'name', 'patronymic']


class Surname(models.Model):
    surname = models.CharField(
        max_length=130, unique=True, null=False, blank=False, verbose_name='Фамилия'
    )

    def __str__(self):
        return self.surname

    class Meta:
        verbose_name = 'Фамилия физического лица'
        verbose_name_plural = 'Фамилии физических лиц'
        # TODO Упорядочивание лучше использовать с помощью Proxy-моделей
        # ordering = ['surname']


class Name(models.Model):
    name = models.CharField(
        max_length=130, unique=True, null=False, blank=False, verbose_name='Имя'
    )

    def __str__(self):
        return self.name

    class Meta:
        verbose_name = 'Имя физического лица'
        verbose_name_plural = 'Имена физических лиц'
        # TODO Упорядочивание лучше использовать с помощью Proxy-моделей
        # ordering = ['name']


class Patronymic(models.Model):
    patronymic = models.CharField(
        max_length=130, unique=True, null=False, blank=False, verbose_name='Фамилия'
    )

    def __str__(self):
        return self.patronymic

    class Meta:
        verbose_name = 'Отчество физического лица'
        verbose_name_plural = 'Отчества физических лиц'
        # TODO Упорядочивание лучше использовать с помощью Proxy-моделей
        # ordering = ['patronymic']
