from django.db import models
from django.contrib.contenttypes.models import ContentType
from django.contrib.contenttypes.fields import GenericForeignKey

from crm.applications.phonebook.nested_models.organization import Organization
from crm.applications.phonebook.nested_models.organization import OrganizationDepartment
from crm.applications.phonebook.nested_models.organization import EmployeePosition
from crm.applications.phonebook.nested_models.organization import Employee

from crm.applications.phonebook.nested_models.person import Person
from crm.applications.phonebook.nested_models.person import PersonSurname
from crm.applications.phonebook.nested_models.person import PersonName
from crm.applications.phonebook.nested_models.person import PersonPatronymic


class Owner(models.Model):
    content_type = models.ForeignKey(ContentType, on_delete=models.CASCADE)
    object_id = models.PositiveIntegerField()
    content_object = GenericForeignKey('content_type', 'object_id', for_concrete_model=False)

    class Meta:
        abstract = True
