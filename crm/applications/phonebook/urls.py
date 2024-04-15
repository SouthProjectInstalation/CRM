from django.urls import path, include

from rest_framework import routers

from crm.applications.phonebook.views import PersonViewSet
from crm.applications.phonebook.views import SurnameViewSet
from crm.applications.phonebook.views import NameViewSet
from crm.applications.phonebook.views import PatronymicViewSet

router = routers.DefaultRouter()
router.register(r'persons', PersonViewSet)
router.register(r'surnames', SurnameViewSet)
router.register(r'names', NameViewSet)
router.register(r'patronymics', PatronymicViewSet)

urlpatterns = [
    path('', include(router.urls))
]
