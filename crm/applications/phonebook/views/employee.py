from rest_framework import viewsets

from crm.applications.phonebook.models import Department
from crm.applications.phonebook.models import Position
from crm.applications.phonebook.models import Employee

from crm.applications.phonebook.serializers import DepartmentSerializer
from crm.applications.phonebook.serializers import PositionSerializer
from crm.applications.phonebook.serializers import EmployeeSerializer


class DepartmentViewSet(viewsets.ModelViewSet):
    queryset = Department.objects.all()
    serializer_class = DepartmentSerializer


class PositionViewSet(viewsets.ModelViewSet):
    queryset = Position.objects.all()
    serializer_class = PositionSerializer


class EmployeeViewSet(viewsets.ModelViewSet):
    queryset = Employee.objects.all()
    serializer_class = EmployeeSerializer

