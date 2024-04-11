from django.db import models

from crm.applications.phonebook.nested_models.person import Person


class Organization(models.Model):
    name = models.CharField(max_length=150, null=False, blank=False)


class OrganizationDepartment(models.Model):
    name = models.CharField(max_length=150, null=True, blank=True)


class EmployeePosition(models.Model):
    position = models.CharField(max_length=150, null=True, blank=True)


class Employee(models.Model):
    organization = models.ForeignKey(Organization, on_delete=models.CASCADE)
    department = models.CharField(max_length=150, null=True, blank=True)
    position = models.CharField(max_length=150, null=True, blank=True)
    person = models.OneToOneField(Person, on_delete=models.CASCADE)
