from django.db import models
from django.db.models import TextChoices


class StatusChoice(TextChoices):
    ACTIVE = 'active', 'Активно'
    NOT_ACTIVE = 'blocked', 'Заблокировано'


# Create your models here.
class Record(models.Model):
    author = models.CharField(max_length=100, null=False, blank=False, verbose_name='Имя автора')
    email = models.EmailField(max_length=254, null=False, blank=False, verbose_name='Почта')
    text = models.CharField(max_length=3000, null=False, blank=False, verbose_name='Текст')
    created_at = models.DateTimeField(auto_now_add=True, verbose_name="Время создания")
    updated_at = models.DateTimeField(auto_now=True, verbose_name="Дата и время редактирования")
    status = models.CharField(verbose_name='Статус',
                              choices=StatusChoice.choices,
                              max_length=20,
                              default=StatusChoice.ACTIVE, null=False
                              )

    def __str__(self):
        return f'{self.author} - {self.email}'
