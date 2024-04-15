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
        'Owner', on_delete=models.CASCADE, related_name='contact_owner', verbose_name='Контактное лицо'
    )
    information = models.ManyToManyField(
        'Information', blank=True, related_name='contact_information', verbose_name='Контактная информация'
    )

    def __str__(self) -> str:
        """
        Возвращает строковое представление контакта.

        :rtype: str
        """
        return f'{self.entity}'

    class Meta:
        verbose_name = 'Контакт'
        verbose_name_plural = 'Контакты'


class Owner(models.Model):
    """
    Модель, представляющая владельца контактной информации в телефонной книге.

    :ivar owner_type: Тип сущности (персона, организация или сотрудник).
    :type owner_type: ForeignKey
    :ivar object_id: Идентификатор объекта сущности.
    :type object_id: PositiveBigIntegerField
    :ivar content_object: Обобщенный ключ для связи с конкретным объектом.
    :type content_object: GenericForeignKey
    """
    owner_type = models.ForeignKey(
        ContentType, on_delete=models.CASCADE,
        limit_choices_to=models.Q(app_label='phonebook', model__in=['person', 'organization', 'employee'])
    )
    object_id = models.PositiveBigIntegerField()
    content_object = GenericForeignKey("owner_type", "object_id")

    def __str__(self) -> str:
        """
        Возвращает строковое представление сущности.

        :rtype: str
        """
        return f'{self.content_object}'

    class Meta:
        constraints = [
            models.UniqueConstraint(fields=['owner_type', 'object_id'], name='unique_contact_entity'),
        ]
        indexes = [
            models.Index(fields=["owner_type", "object_id"]),
        ]


class Information(models.Model):
    """
    Модель, представляющая контактную информацию.

    :ivar information_type: Тип информации (телефон, электронная почта и т. д.).
    :type information_type: ForeignKey
    :ivar object_id: Идентификатор объекта контактной информации.
    :type object_id: PositiveBigIntegerField
    :ivar content_object: Обобщенный ключ для связи с конкретным объектом.
    :type content_object: GenericForeignKey
    """
    information_type = models.ForeignKey(
        ContentType, on_delete=models.CASCADE,
        limit_choices_to=models.Q(app_label='phonebook', model__in=[])
    )
    object_id = models.PositiveBigIntegerField()
    content_object = GenericForeignKey("information_type", "object_id")

    def __str__(self) -> str:
        """
        Возвращает строковое представление контактной информации.

        :rtype: str
        """
        return f'{self.content_object}'

    class Meta:
        constraints = [
            models.UniqueConstraint(fields=['information_type', 'object_id'], name='unique_contact_info'),
        ]
        indexes = [
            models.Index(fields=["information_type", "object_id"]),
        ]
