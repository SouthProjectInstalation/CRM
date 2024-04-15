from django.db import models

from crm.applications.phonebook.models import Organization
from crm.applications.phonebook.models import Person


class Employee(models.Model):
    organization = models.ForeignKey(Organization, on_delete=models.CASCADE, verbose_name='Организация')
    department = models.ForeignKey('Department', on_delete=models.CASCADE, verbose_name='Подразделение')
    position = models.ForeignKey('Position', on_delete=models.CASCADE, verbose_name='Должность')
    person = models.OneToOneField(Person, on_delete=models.CASCADE, verbose_name='Физическое лицо')

    def __str__(self):
        return f'{self.organization}, {self.department}, {self.position}, {self.person}'

    class Meta:
        verbose_name = 'Сотрудник организации'
        verbose_name_plural = 'Сотрудники организаций'
        # TODO Упорядочивание лучше использовать с помощью Proxy-моделей
        # ordering = ['organization', 'person.surname', 'person.name', 'person.patronymic']


class Position(models.Model):
    position = models.CharField(
        max_length=150, unique=True, null=True, blank=True, verbose_name='Должность сотрудника'
    )

    def __str__(self):
        return self.position

    class Meta:
        verbose_name = 'Должность сотрудника'
        verbose_name_plural = 'Должности сотрудников'
        # TODO Упорядочивание лучше использовать с помощью Proxy-моделей
        # ordering = ['position']


class Department(models.Model):
    department = models.CharField(
        max_length=150, unique=True, null=True, blank=True, verbose_name='Название подразделения'
    )

    def __str__(self):
        return self.department

    class Meta:
        verbose_name = 'Подразделение организации'
        verbose_name_plural = 'Подразделения организаций'
        # TODO Упорядочивание лучше использовать с помощью Proxy-моделей
        # ordering = ['department']
