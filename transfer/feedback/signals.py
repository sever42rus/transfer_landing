from django.conf import settings
from django.core.mail import send_mail 

from django.db.models.signals import post_save
from django.db import transaction
from django.dispatch import receiver

from .models import Feedback
from settings.models import TelegramBot

import telebot

MESSAGE = """
Имя:{0}
Email:{1}
Телефон:{2}
Сообщение:{3}
Дата:{4}
"""


def send_tele_bot_and_email(feedback, bot_settings):
	message = MESSAGE.format(feedback.name, feedback.email, feedback.telephone, feedback.message, feedback.datetime_create.strftime('%d/%m/%Y %H:%M'))
	try:
		bot = telebot.TeleBot(bot_settings.token)
		for chenal in bot_settings.chenal.all():
			try:
				bot.send_message(chenal.chenal_id , message)
			except:
				print('Проверьте настройки бота! отправка сообщения в канал!')
		
		for chat in bot_settings.chat.all():
			try:
				bot.send_message(chat.chat_id , message)
			except:
				print('Проверьте настройки бота! отправка сообщения в ПМ!')
	except:
		print('Проверьте настройки бота')

	send_mail_valid = send_mail('Регистрация на сайте', message, settings.EMAIL_HOST_USER, [settings.DEFAULT_FROM_EMAIL], fail_silently=True)
	if not send_mail_valid:
		print('Проверьте настройки почты!')

@receiver(post_save, sender=Feedback)
def send_telegramm(sender, instance, created, **kwargs):
	if created:
		telegram_bot = TelegramBot.objects.first()
		transaction.on_commit(lambda: send_tele_bot_and_email(instance, telegram_bot))
