from uuid import uuid4

from ckeditor.fields import RichTextField
from django.db import models
from django.utils import timezone
from feedback.models import Feedback

# Create your models here.


class Recall(models.Model):
    TITLE_CHOICES = [
        ('Очень хорошо!', 'Очень хорошо!'),
        ('Хорошо!', 'Хорошо!'),
        ('Удовлетворительно!', 'Удовлетворительно!'),
        ('Плохо!', 'Плохо!'),
        ('Очень плохо!', 'Очень плохо!'),
    ]

    feedback = models.ForeignKey(Feedback, on_delete=models.CASCADE,
                                 verbose_name='Заявка обратной связи', related_name='recall')
    title = models.CharField(
        max_length=20, choices=TITLE_CHOICES, verbose_name='Заголовок',)
    text = models.CharField(max_length=200, verbose_name='Отзыв',)
    verified = models.BooleanField(default=False, verbose_name='Верификация',)

    datetime_create = models.DateTimeField(
        default=timezone.now, verbose_name='Дата и время создания',)
    datetime_update = models.DateTimeField(
        auto_now=True, verbose_name='Дата и время последнего изменения')

    class Meta:
        verbose_name_plural = 'Отзывы'
        verbose_name = 'Отзыв'

    def __str__(self):
        return self.title


class RecallInvite(models.Model):
    id = models.UUIDField(primary_key=True, default=uuid4, editable=False)
    feedback = models.ForeignKey(Feedback, on_delete=models.CASCADE,
                                 verbose_name='Заявка обратной связи', related_name='recall_invite')
    done = models.BooleanField(default=False, verbose_name='Выполнено',)
