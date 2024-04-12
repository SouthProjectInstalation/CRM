from rest_framework import serializers

from crm.applications.phonebook.nested_models.person import Person, PersonSurname, PersonName, PersonPatronymic


class PersonSerializer(serializers.ModelSerializer):
    class Meta:
        model = Person
        fields = '__all__'


class PersonSurnameSerializer(serializers.ModelSerializer):
    class Meta:
        model = PersonSurname
        fields = '__all__'


class PersonNameSerializer(serializers.ModelSerializer):
    class Meta:
        model = PersonName
        fields = '__all__'


class PersonPatronymicSerializer(serializers.ModelSerializer):
    class Meta:
        model = PersonPatronymic
        fields = '__all__'
