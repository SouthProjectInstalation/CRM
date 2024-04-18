from rest_framework import serializers

from crm.applications.phonebook.models import Owner, Information, Contact

from crm.applications.phonebook.serializers import ContentTypeSerializer

from crm.applications.phonebook.models import Person, Organization, Employee
from crm.applications.phonebook.serializers import PersonSerializer, OrganizationSerializer, EmployeeSerializer

# from crm.applications.phonebook.models import Email, Phone, Social, Messanger
# from crm.applications.phonebook.serializers import EmailSerializer, PhoneSerializer, SocialSerializer
# from crm.applications.phonebook.serializers import MessangerSerializer


class GenericSerializer(serializers.Serializer):
    type = ContentTypeSerializer(read_only=True)
    content = serializers.SerializerMethodField()

    class Meta:
        model = Owner
        fields = ['type', 'content']


class OwnerSerializer(GenericSerializer):

    def get_content(self, obj):
        content = obj.content_object
        match content:
            case Person():
                return PersonSerializer(content).data
            case Organization():
                return OrganizationSerializer(content).data
            case Employee():
                return EmployeeSerializer(content).data
            case _:
                return None


# class InformationSerializer(GenericSerializer):
#
#     def get_content(self, obj):
#         content = obj.content_object
#         match content:
#             case Email():
#                 return EmailSerializer(content).data
#             case Phone():
#                 return PhoneSerializer(content).data
#             case Social():
#                 return SocialSerializer(content).data
#             case Messanger():
#                 return MessangerSerializer(content).data
#             case _:
#                 return None


class ContactSerializer(serializers.ModelSerializer):
    owner = OwnerSerializer(read_only=True)
    # information = InformationSerializer(read_only=True)

    class Meta:
        model = Contact
        fields = '__all__'
