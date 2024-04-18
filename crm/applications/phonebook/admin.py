from django.contrib import admin

from crm.applications.phonebook.models import Person
from crm.applications.phonebook.models import Surname
from crm.applications.phonebook.models import Name
from crm.applications.phonebook.models import Patronymic

from crm.applications.phonebook.models import Organization

from crm.applications.phonebook.models import Department
from crm.applications.phonebook.models import Position
from crm.applications.phonebook.models import Employee

from crm.applications.phonebook.models import Contact
from crm.applications.phonebook.models import Owner
from crm.applications.phonebook.models import Information

from crm.applications.phonebook.models import Alias
from crm.applications.phonebook.models import Email
from crm.applications.phonebook.models import Phone
from crm.applications.phonebook.models import Social
from crm.applications.phonebook.models import Messanger


admin.site.register(
    [
        Person,
        Surname,
        Name,
        Patronymic,

        Organization,
        Department,
        Position,
        Employee,

        Contact,
        Owner,
        Information,

        Alias,
        Email,
        Phone,
        Social,
        Messanger,
    ]
)
