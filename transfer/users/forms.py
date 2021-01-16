from django import forms

from django.contrib.auth.forms import UserCreationForm, UserChangeForm
from django.core.exceptions import ValidationError
from .models import User

class UserCreationForm(UserCreationForm):
	class Meta:
		model = User
		fields = ('email', 'password1', 'password2')

	"""def __init__(self, *args, **kwargs):
		super(CustomUserCreationForm, self).__init__(*args, **kwargs)

		self.fields['email'].widget.attrs['class'] = 'form-control'
		self.fields['password1'].widget.attrs['class'] = 'form-control'
		self.fields['password2'].widget.attrs['class'] = 'form-control'"""

	def clean_email(self):
		new_email = self.cleaned_data['email'].lower()
		return new_email

	def save(self, commit=True):
		user = super(UserCreationForm, self).save(commit=False)
		user.email = self.cleaned_data["email"]
		user.set_password(self.cleaned_data["password1"])
		user.is_active = False
		user.is_staff = False
		user.is_superuser = False
		if commit:
			user.save()
		return user
        
class UserChangeForm(forms.ModelForm):
	class Meta:
		model = User
		fields = ('first_name', 'middle_name', 'last_name')


class LoginForm(forms.Form):
	email = forms.EmailField()
	password = forms.CharField(widget=forms.PasswordInput)

	def clean_email(self):
		new_email = self.cleaned_data['email'].lower()
		return new_email