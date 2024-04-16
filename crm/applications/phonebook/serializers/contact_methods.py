from rest_framework import serializers

from crm.applications.phonebook.models import Alias, Email, Phone, Social, Messanger


class AliasSerializer(serializers.ModelSerializer):
    class Meta:
        model = Alias
        fields = '__all__'


class EmailSerializer(serializers.ModelSerializer):
    class Meta:
        model = Email
        fields = '__all__'


class PhoneSerializer(serializers.ModelSerializer):
    class Meta:
        model = Phone
        fields = '__all__'


class SocialSerializer(serializers.ModelSerializer):
    class Meta:
        model = Social
        fields = '__all__'


class MessangerSerializer(serializers.ModelSerializer):
    class Meta:
        model = Messanger
        fields = '__all__'
