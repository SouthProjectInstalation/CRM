from django.db import models

from django.contrib.contenttypes.fields import GenericForeignKey
from django.contrib.contenttypes.models import ContentType


class Contact(models.Model):
    """
    Модель, представляющая собой контакт в телефонной книге.

    :ivar entity: Контактное лицо, связанное с данным контактом.
    :type entity: OneToOneField
    :ivar information: Контактная информация, связанная с данным контактом.
    :type information: ManyToManyField
    """
    entity = models.OneToOneField(
        'Owner', on_delete=models.CASCADE, related_name='phonebook_contact_owner', verbose_name='контактное лицо'
    )
    information = models.ManyToManyField(
        'Information', blank=True, related_name='phonebook_contact_information', verbose_name='контактная информация'
    )

    def __str__(self) -> str:
        """
        Возвращает строковое представление контакта.

        :rtype: str
        """
        return f'{self.entity}'

    class Meta:
        verbose_name = 'контакт'
        verbose_name_plural = 'контакты'


class Owner(models.Model):
    """
    Модель, представляющая владельца контактной информации в телефонной книге.

    :ivar type: Тип сущности (персона, организация или сотрудник).
    :type type: ForeignKey
    :ivar object_id: Идентификатор объекта сущности.
    :type object_id: PositiveBigIntegerField
    :ivar content_object: Обобщенный ключ для связи с конкретным объектом.
    :type content_object: GenericForeignKey
    """
    type = models.ForeignKey(
        ContentType, on_delete=models.CASCADE, verbose_name='тип контактного лица',
        limit_choices_to=models.Q(app_label='phonebook', model__in=['person', 'organization', 'employee'])
    )
    object_id = models.PositiveBigIntegerField()
    content_object = GenericForeignKey("type", "object_id")

    def __str__(self) -> str:
        """
        Возвращает строковое представление сущности.

        :rtype: str
        """
        return f'{self.content_object}'

    class Meta:
        verbose_name = 'контактное лицо'
        verbose_name_plural = 'контактные лица'
        constraints = [
            models.UniqueConstraint(fields=['type', 'object_id'], name='phonebook_owner_unique'),
        ]
        indexes = [
            models.Index(fields=["type", "object_id"], name='phonebook_owner_index'),
        ]


class Information(models.Model):
    """
    Модель, представляющая контактную информацию.

    :ivar type: Тип информации (телефон, электронная почта и т. д.).
    :type type: ForeignKey
    :ivar object_id: Идентификатор объекта контактной информации.
    :type object_id: PositiveBigIntegerField
    :ivar content_object: Обобщенный ключ для связи с конкретным объектом.
    :type content_object: GenericForeignKey
    """
    type = models.ForeignKey(
        ContentType, on_delete=models.CASCADE, verbose_name='контактная информация',
        limit_choices_to=models.Q(app_label='phonebook', model__in=['email', 'phone', 'social', 'messanger'])
    )
    object_id = models.PositiveBigIntegerField()
    content_object = GenericForeignKey("type", "object_id")

    def __str__(self) -> str:
        """
        Возвращает строковое представление контактной информации.

        :rtype: str
        """
        return f'{self.content_object}'

    class Meta:
        verbose_name = 'контактная информация'
        verbose_name_plural = 'контактная информация'
        constraints = [
            models.UniqueConstraint(fields=['type', 'object_id'], name='phonebook_information_unique'),
        ]
        indexes = [
            models.Index(fields=["type", "object_id"], name='phonebook_information_index'),
        ]
