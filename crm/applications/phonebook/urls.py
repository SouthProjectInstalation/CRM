from django.urls import path, include

from rest_framework import routers

from crm.applications.phonebook.views import PersonViewSet
from crm.applications.phonebook.views import PersonSurnameViewSet
from crm.applications.phonebook.views import PersonNameViewSet
from crm.applications.phonebook.views import PersonPatronymicViewSet

router = routers.DefaultRouter()
router.register(r'persons', PersonViewSet)
router.register(r'surnames', PersonSurnameViewSet)
router.register(r'names', PersonNameViewSet)
router.register(r'patronymics', PersonPatronymicViewSet)

urlpatterns = [
    path('', include(router.urls))
]
