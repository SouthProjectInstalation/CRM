from rest_framework import serializers

from crm.applications.phonebook.models import Person, Surname, Name, Patronymic


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


class PersonSerializer(serializers.ModelSerializer):
    surname = serializers.CharField()
    name = serializers.CharField()
    patronymic = serializers.CharField()

    class Meta:
        model = Person
        fields = '__all__'
