from ckeditor.fields import RichTextField
from django.db import models

# Create your models here.


class Setting(models.Model):
    site_title = models.CharField(
        max_length=20, verbose_name='Название сайта',)
    telephone_num = models.CharField(
        max_length=20, verbose_name='Телефонный номер',)
    email = models.EmailField(verbose_name='Email',)

    org_name = models.CharField(
        blank=True, null=True, max_length=20, verbose_name='Название организации',)

    top_img = models.ImageField(upload_to='setting', blank=True,
                                null=True, verbose_name='Изображение в верхнем разделе',)
    favicon = models.ImageField(
        upload_to='setting', blank=True, null=True, verbose_name='favicon',)
    logo_top = models.ImageField(
        upload_to='setting', blank=True, null=True, verbose_name='Логотип в шапке',)

    class Meta:
        verbose_name_plural = 'Основные настройки'
        verbose_name = 'Основные настройки'

    def delete(self, *args, **kwargs):
        pass

    def save(self, *args, **kwargs):
        self.pk = 1
        self.__class__.objects.all().delete()
        super().save(*args, **kwargs)

    def __str__(self):
        return "Основные настройки"


class About(models.Model):
    title = models.CharField(max_length=30, verbose_name='Заголовок',)
    text = RichTextField(verbose_name='Текст',)

    class Meta:
        verbose_name_plural = "Разделы 'О Нас"
        verbose_name = "Раздел 'О Нас"

    def __str__(self):
        return self.title


SOCIAL_NETWORK_CHOICES = [
    ('fab fa-fw fa-whatsapp', 'whatsapp'),
    ('fab fa-fw fa-viber', 'viber'),
    ('fab fa-fw fa-telegram-plane', 'telegram'),
    ('fab fa-fw fa-instagram', 'instagram'),
    ('fab fa-fw fa-vk', 'vk'),
    ('fab fa-fw fa-facebook-f', 'facebook'),
    ('fab fa-fw fa-odnoklassniki', 'odnoklassniki'),
    ('fab fa-fw fa-twitter', 'twitter'),
    ('fab fa-fw fa-youtube', 'youtube'),
]


class SocialNetwork(models.Model):
    name = models.CharField(
        max_length=512, choices=SOCIAL_NETWORK_CHOICES, verbose_name='Название соц. сети',)
    link = models.CharField(max_length=512, verbose_name='Ссылка',)

    class Meta:
        verbose_name_plural = 'Социальные сети'
        verbose_name = 'Социальные сети'

    def __str__(self):
        return str(self.name)


class TelegramBot(models.Model):
    token = models.CharField(max_length=150, verbose_name='Токен бота',)

    class Meta:
        verbose_name_plural = 'Настройки telegram бота'
        verbose_name = 'Настройки telegram бота'

    def delete(self, *args, **kwargs):
        pass

    def save(self, *args, **kwargs):
        self.pk = 1
        # self.__class__.objects.all().delete()
        super().save(*args, **kwargs)

    def __str__(self):
        return "Настройки Telegram бота"


class TelegramChenalID(models.Model):
    tele_bot = models.ForeignKey(
        TelegramBot, on_delete=models.CASCADE, related_name='chat')
    chat_id = models.CharField(max_length=150, verbose_name='ID чата',)

    class Meta:
        verbose_name_plural = 'Чат'
        verbose_name = 'Чаты'

    def __str__(self):
        return ""


class TelegramChatID(models.Model):
    tele_bot = models.ForeignKey(
        TelegramBot, on_delete=models.CASCADE, related_name='chenal')
    chenal_id = models.CharField(max_length=150, verbose_name='ID канала',)

    class Meta:
        verbose_name_plural = 'Канал'
        verbose_name = 'Каналы'

    def __str__(self):
        return ""
