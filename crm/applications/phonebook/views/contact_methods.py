from rest_framework import viewsets

from crm.applications.phonebook.models import Alias
from crm.applications.phonebook.models import Email
from crm.applications.phonebook.models import Phone
from crm.applications.phonebook.models import Social
from crm.applications.phonebook.models import Messanger

from crm.applications.phonebook.serializers import AliasSerializer
from crm.applications.phonebook.serializers import EmailSerializer
from crm.applications.phonebook.serializers import PhoneSerializer
from crm.applications.phonebook.serializers import SocialSerializer
from crm.applications.phonebook.serializers import MessangerSerializer


class AliasViewSet(viewsets.ModelViewSet):
    queryset = Alias.objects.all()
    serializer_class = AliasSerializer


class EmailViewSet(viewsets.ModelViewSet):
    queryset = Email.objects.all()
    serializer_class = EmailSerializer


class PhoneViewSet(viewsets.ModelViewSet):
    queryset = Phone.objects.all()
    serializer_class = PhoneSerializer


class SocialViewSet(viewsets.ModelViewSet):
    queryset = Social.objects.all()
    serializer_class = SocialSerializer


class MessangerViewSet(viewsets.ModelViewSet):
    queryset = Messanger.objects.all()
    serializer_class = MessangerSerializer
