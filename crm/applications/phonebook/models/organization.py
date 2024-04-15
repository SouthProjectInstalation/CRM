from django.db import models


class Organization(models.Model):
    name = models.CharField(
        max_length=150, null=False, blank=False, verbose_name='Название организации'
    )

    def __str__(self):
        return self.name

    class Meta:
        verbose_name = 'Организация'
        verbose_name_plural = 'Организации'
        # TODO Упорядочивание лучше использовать с помощью Proxy-моделей
        # ordering = ['name']
