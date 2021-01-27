from datetime import datetime

from django.db import models
from django.utils import timezone

# Create your models here.


class Feedback(models.Model):
    name = models.CharField(max_length=150, verbose_name='ФИО',)
    email = models.EmailField(verbose_name='Email',)
    telephone = models.CharField(
        max_length=20, verbose_name='Телефонный номер',)
    message = models.TextField(verbose_name='Сообщение',)
    in_work = models.BooleanField(default=False, verbose_name='В работе',)
    performed = models.BooleanField(default=False, verbose_name='Выполнено',)
    datetime_create = models.DateTimeField(
        default=timezone.now, verbose_name='Дата и время создания',)
    datetime_update = models.DateTimeField(
        auto_now=True, verbose_name='Дата и время последнего изменения')

    class Meta:
        verbose_name_plural = 'Заявки (Обратная связь)'
        verbose_name = 'Заявка (Обратная связь)'

    def __str__(self):
        return self.name + ' ' + self.telephone


class Comment(models.Model):
    feedback = models.ForeignKey(Feedback, on_delete=models.CASCADE,
                                 verbose_name='Заявка обратной связи', related_name='comment')
    comment = models.TextField(verbose_name='Комментарий',)
    datetime_create = models.DateTimeField(
        default=timezone.now, verbose_name='Дата и время создания',)

    class Meta:
        verbose_name_plural = 'Комментарии'
        verbose_name = 'Комментарий'

    def __str__(self):
        date_time = timezone.localtime(self.datetime_create)
        return 'Комментарии от ' + datetime.strftime(date_time, '%Y-%m-%d %H:%M')
