from django.db import models

from django.contrib.contenttypes.models import ContentType

from phonenumber_field.modelfields import PhoneNumberField


class Alias(models.Model):
    type = models.ForeignKey(
        ContentType, on_delete=models.CASCADE, verbose_name='тип способа связи',
        limit_choices_to=models.Q(app_label='phonebook', model__in=['email', 'phone', 'social', 'messanger'])
    )
    alias = models.CharField(max_length=64, verbose_name='псевдоним способа связи')
    
    def __str__(self):
        return f'{self.type}: {self.alias}'
    
    class Meta:
        verbose_name = 'псевдоним способа связи'
        verbose_name_plural = 'псевдонимы способов связи'
        constraints = [
            models.UniqueConstraint(fields=['type', 'alias'], name='phonebook_alias_unique'),
        ]
        indexes = [
            models.Index(fields=['type', 'alias'], name='phonebook_alias_index'),
        ]


class ContactAlias(models.Model):
    alias = models.ForeignKey(Alias, on_delete=models.CASCADE, verbose_name='псевдоним способа связи')

    class Meta:
        abstract = True


class Email(ContactAlias):
    address = models.EmailField(blank=False, verbose_name='адрес электронной почты')

    def __str__(self):
        return f'{self.alias} {self.address}'

    class Meta:
        verbose_name = 'адрес электронной почты'
        verbose_name_plural = 'адреса электронной почты'
        constraints = [
            models.UniqueConstraint(fields=['address'], name='phonebook_email_unique'),
        ]
        indexes = [
            models.Index(fields=['alias', 'address'], name='phonebook_email_index'),
        ]


class Phone(ContactAlias):
    number = PhoneNumberField(blank=False, verbose_name='номер телефона')

    def __str__(self):
        return f'{self.alias} {self.number}'

    class Meta:
        verbose_name = 'номер телефона'
        verbose_name_plural = 'номера телефонов'
        constraints = [
            models.UniqueConstraint(fields=['number'], name='phonebook_phone_unique'),
        ]
        indexes = [
            models.Index(fields=['alias', 'number'], name='phonebook_phone_index'),
        ]


class Social(ContactAlias):
    url = models.URLField(verbose_name='ссылка на профиль')

    def __str__(self):
        return f'{self.alias} {self.url}'

    class Meta:
        verbose_name = 'социальное пространство'
        verbose_name_plural = 'социальные пространства'
        constraints = [
            models.UniqueConstraint(fields=['url'], name='phonebook_social_unique'),
        ]
        indexes = [
            models.Index(fields=['alias', 'url'], name='phonebook_social_index'),
        ]


class Messanger(ContactAlias):
    link = models.URLField(verbose_name='ссылка на профиль')

    def __str__(self):
        return f'{self.alias} {self.link}'

    class Meta:
        verbose_name = 'мессенджер'
        verbose_name_plural = 'мессенджеры'
        constraints = [
            models.UniqueConstraint(fields=['link'], name='phonebook_messanger_unique'),
        ]
        indexes = [
            models.Index(fields=['alias', 'link'], name='phonebook_messanger_index'),
        ]
    
    
