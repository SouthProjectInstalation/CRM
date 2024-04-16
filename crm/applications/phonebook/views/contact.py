from rest_framework import viewsets

from crm.applications.phonebook.models import Contact
from crm.applications.phonebook.models import Owner
from crm.applications.phonebook.models import Information

from crm.applications.phonebook.serializers import ContactSerializer
from crm.applications.phonebook.serializers import OwnerSerializer
from crm.applications.phonebook.serializers import InformationSerializer


class ContactViewSet(viewsets.ModelViewSet):
    queryset = Contact.objects.all()
    serializer_class = ContactSerializer


class OwnerViewSet(viewsets.ModelViewSet):
    queryset = Owner.objects.all()
    serializer_class = OwnerSerializer


class InformationViewSet(viewsets.ModelViewSet):
    queryset = Information.objects.all()
    serializer_class = InformationSerializer
