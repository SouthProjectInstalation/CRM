from rest_framework import viewsets

from crm.applications.phonebook.models import Person
from crm.applications.phonebook.models import PersonSurname
from crm.applications.phonebook.models import PersonName
from crm.applications.phonebook.models import PersonPatronymic

from crm.applications.phonebook.serializers import PersonSerializer
from crm.applications.phonebook.serializers import PersonSurnameSerializer
from crm.applications.phonebook.serializers import PersonNameSerializer
from crm.applications.phonebook.serializers import PersonPatronymicSerializer


class PersonViewSet(viewsets.ModelViewSet):
    queryset = Person.objects.all()
    serializer_class = PersonSerializer


class PersonSurnameViewSet(viewsets.ModelViewSet):
    queryset = PersonSurname.objects.all()
    serializer_class = PersonSurnameSerializer


class PersonNameViewSet(viewsets.ModelViewSet):
    queryset = PersonName.objects.all()
    serializer_class = PersonNameSerializer


class PersonPatronymicViewSet(viewsets.ModelViewSet):
    queryset = PersonPatronymic.objects.all()
    serializer_class = PersonPatronymicSerializer
