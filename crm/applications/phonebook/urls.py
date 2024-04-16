from django.urls import path, include

from rest_framework import routers

from crm.applications.phonebook.views import PersonViewSet
from crm.applications.phonebook.views import SurnameViewSet
from crm.applications.phonebook.views import NameViewSet
from crm.applications.phonebook.views import PatronymicViewSet

from crm.applications.phonebook.views import OrganizationViewSet

from crm.applications.phonebook.views import DepartmentViewSet
from crm.applications.phonebook.views import PositionViewSet
from crm.applications.phonebook.views import EmployeeViewSet

from crm.applications.phonebook.views import ContactViewSet
from crm.applications.phonebook.views import OwnerViewSet
from crm.applications.phonebook.views import InformationViewSet

from crm.applications.phonebook.views import AliasViewSet
from crm.applications.phonebook.views import EmailViewSet
from crm.applications.phonebook.views import PhoneViewSet
from crm.applications.phonebook.views import SocialViewSet
from crm.applications.phonebook.views import MessangerViewSet

router = routers.DefaultRouter()

router.register(r'persons', PersonViewSet)
router.register(r'surnames', SurnameViewSet)
router.register(r'names', NameViewSet)
router.register(r'patronymics', PatronymicViewSet)

router.register(r'organizations', OrganizationViewSet)

router.register(r'departments', DepartmentViewSet)
router.register(r'positions', PositionViewSet)
router.register(r'employees', EmployeeViewSet)

router.register(r'contacts', ContactViewSet)
router.register(r'owners', OwnerViewSet)
router.register(r'information', InformationViewSet)

router.register(r'alias', AliasViewSet)
router.register(r'emails', EmailViewSet)
router.register(r'phones', PhoneViewSet)
router.register(r'socials', SocialViewSet)
router.register(r'messangers', MessangerViewSet)

urlpatterns = [
    path('', include(router.urls))
]
