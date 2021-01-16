import uuid
from django.conf import settings
from django.db import models
from django.utils import timezone
from django.urls import reverse

from django.contrib.auth.models import AbstractUser, BaseUserManager, Group

class CustomUserManager(BaseUserManager):

	def normalize_email(self, email):
		return email.lower()

	def _create_user(self, email, password, is_active, is_staff, is_superuser, **extra_fields):
		now = timezone.now()
		email = self.normalize_email(email)

		user = User(email=email, is_active=is_active, is_staff=is_staff, is_superuser=is_superuser, date_joined=now, **extra_fields)
		user.set_password(password)
		user.save()
		return user

	def create_user(self, email, password, **extra_fields):
		return self._create_user(email, password, False, False, False, **extra_fields)

	def create_superuser(self, email, password, **extra_fields):
		return self._create_user(email, password, True, True, True, **extra_fields)

# Create your models here.
class User(AbstractUser):
	username = None
	email = models.EmailField(unique=True, verbose_name='Email') # changes email to unique and blank to false

	USERNAME_FIELD = 'email'
	REQUIRED_FIELDS = [] # removes email from REQUIRED_FIELDS

	objects = CustomUserManager()

	id = models.UUIDField(primary_key=True, default=uuid.uuid4, editable=False)
	middle_name = models.CharField(max_length = 50, blank=True, verbose_name = 'Отчество',)

	def __str__(self):
		return self.email

	class Meta:
		verbose_name = 'Пользователь'
		verbose_name_plural = 'Пользователи'

class UserGroup(Group):
	# только для админки

	class Meta:
		proxy = True
		verbose_name = 'Группа'
		verbose_name_plural = 'Группы'