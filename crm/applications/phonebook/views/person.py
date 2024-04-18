from rest_framework import viewsets

from crm.applications.phonebook.models import Person
from crm.applications.phonebook.models import Surname
from crm.applications.phonebook.models import Name
from crm.applications.phonebook.models import Patronymic

from crm.applications.phonebook.serializers import PersonSerializer
from crm.applications.phonebook.serializers import SurnameSerializer
from crm.applications.phonebook.serializers import NameSerializer
from crm.applications.phonebook.serializers import PatronymicSerializer


class PersonViewSet(viewsets.ModelViewSet):
    queryset = Person.objects.all()
    serializer_class = PersonSerializer


class SurnameViewSet(viewsets.ModelViewSet):
    queryset = Surname.objects.all()
    serializer_class = SurnameSerializer


class NameViewSet(viewsets.ModelViewSet):
    queryset = Name.objects.all()
    serializer_class = NameSerializer


class PatronymicViewSet(viewsets.ModelViewSet):
    queryset = Patronymic.objects.all()
    serializer_class = PatronymicSerializer

