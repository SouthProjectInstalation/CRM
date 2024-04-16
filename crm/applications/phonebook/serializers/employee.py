from rest_framework import serializers

from crm.applications.phonebook.models import Department, Position, Employee

from crm.applications.phonebook.serializers import OrganizationSerializer
from crm.applications.phonebook.serializers import PersonSerializer


class DepartmentSerializer(serializers.ModelSerializer):
    class Meta:
        model = Department
        fields = '__all__'


class PositionSerializer(serializers.ModelSerializer):
    class Meta:
        model = Position
        fields = '__all__'


class EmployeeSerializer(serializers.ModelSerializer):
    organization = OrganizationSerializer(read_only=True)
    department = DepartmentSerializer(read_only=True)
    position = PositionSerializer(read_only=True)
    person = PersonSerializer(read_only=True)

    class Meta:
        model = Employee
        fields = '__all__'
