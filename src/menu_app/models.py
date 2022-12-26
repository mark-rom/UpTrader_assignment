from django.db import models


class Menu(models.Model):
    name = models.CharField(
        verbose_name='Название меню',
        max_length=60,
        help_text='Обязательное поле'
    )
    slug = models.SlugField(
        verbose_name='Уникальный слаг меню',
        unique=True,
        help_text='Обязательное поле'
    )

    class Meta:
        verbose_name = 'Меню'
        verbose_name_plural = 'Меню'

    def __str__(self) -> str:
        return self.name


class MenuItem(models.Model):
    name = models.CharField(
        verbose_name='Название пункта меню',
        max_length=60,
        help_text='Обязательное поле'
    )
    path = models.CharField(
        verbose_name='Относительный путь к странице',
        max_length=30, blank=True,
        help_text='Пустое для первого уровня меню'
    )
    parent = models.ForeignKey(
        'self',
        verbose_name='Предыдущий уровень меню',
        blank=True, null=True,
        default=None, on_delete=models.CASCADE,
        help_text='Пустое для первого уровня меню'
    )
    menu = models.ForeignKey(
        Menu,
        verbose_name='Меню к которому привязан пункт',
        on_delete=models.CASCADE,
        help_text='Обязательное поле'
    )

    class Meta:
        verbose_name = 'Пункт меню'
        verbose_name_plural = 'Пункты меню'

    def __str__(self) -> str:
        return self.name
