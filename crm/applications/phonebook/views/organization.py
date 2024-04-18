from rest_framework import viewsets

from crm.applications.phonebook.models import Organization

from crm.applications.phonebook.serializers import OrganizationSerializer


class OrganizationViewSet(viewsets.ModelViewSet):
    queryset = Organization.objects.all()
    serializer_class = OrganizationSerializer
