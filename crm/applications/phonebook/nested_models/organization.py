from django.db import models

from crm.applications.phonebook.nested_models.person import Person


class Organization(models.Model):
    name = models.CharField(max_length=150, null=False, blank=False, verbose_name='Название организации')

    class Meta:
        verbose_name = 'Организация'
        verbose_name_plural = 'Организации'
        ordering = ['name']


class OrganizationDepartment(models.Model):
    department = models.CharField(max_length=150, unique=True, null=True, blank=True, verbose_name='Название подразделения')

    class Meta:
        verbose_name = 'Подразделение организации'
        verbose_name_plural = 'Подразделения организаций'
        ordering = ['department']


class EmployeePosition(models.Model):
    position = models.CharField(max_length=150, unique=True, null=True, blank=True, verbose_name='Должность сотрудника')

    class Meta:
        verbose_name = 'Должность сотрудника'
        verbose_name_plural = 'Должности сотрудников'
        ordering = ['position']


class Employee(models.Model):
    organization = models.ForeignKey(Organization, on_delete=models.CASCADE, verbose_name='Организация')
    department = models.ForeignKey(OrganizationDepartment, on_delete=models.CASCADE, verbose_name='Подразделение')
    position = models.ForeignKey(EmployeePosition, on_delete=models.CASCADE, verbose_name='Должность')
    person = models.OneToOneField(Person, on_delete=models.CASCADE, verbose_name='Физическое лицо')

    class Meta:
        verbose_name = 'Сотрудник организации'
        verbose_name_plural = 'Сотрудники организаций'
        ordering = ['organization', 'person.surname', 'person.name', 'person.patronymic']
