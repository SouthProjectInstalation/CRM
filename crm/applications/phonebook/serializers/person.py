from rest_framework import serializers

from crm.applications.phonebook.models import Person, Surname, Name, Patronymic


class PersonSerializer(serializers.ModelSerializer):
    class Meta:
        model = Person
        fields = '__all__'


class SurnameSerializer(serializers.ModelSerializer):
    class Meta:
        model = Surname
        fields = '__all__'


class NameSerializer(serializers.ModelSerializer):
    class Meta:
        model = Name
        fields = '__all__'


class PatronymicSerializer(serializers.ModelSerializer):
    class Meta:
        model = Patronymic
        fields = '__all__'
