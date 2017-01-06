from django import forms 
from django.contrib.auth.models import User
from .models import Administrator, Client

class UserRegistrationForm(forms.ModelForm):
	password = forms.CharField(label="Contraseña", widget=forms.PasswordInput)
	password2 = forms.CharField(label="Repite tu Contraseña", widget=forms.PasswordInput)

	class Meta:
		model = User;
		fields = ('username', 'email')
		help_texts = {
			'username' : None,
		}

	def clean_password2(self):
		clean = self.cleaned_dhata
		if clean['password']!= clean['password2']:
			raise forms.ValidationError("Las contraseñas no coinciden")
		return clean['password2']

class UserRegistrationClientForm(forms.ModelForm):
	# password = forms.CharField(label="Contraseña", widget=forms.PasswordInput)
	# password2 = forms.CharField(label="Repite tu Contraseña", widget=forms.PasswordInput)

	class Meta:
		model = User;
		fields = ('first_name', 'last_name')
		# help_texts = {
		# 	'username' : None,
		# }

	# def clean_password2(self):
	# 	clean = self.cleaned_dhata
	# 	if clean['password']!= clean['password2']:
	# 		raise forms.ValidationError("Las contraseñas no coinciden")
	# 	return clean['password2']

class AdminForm(forms.ModelForm):
	class Meta:
		model = Administrator
		fields = (
			'administrator_root',
			)

class ClientForm(forms.ModelForm):
	class Meta:
		model = Client
		fields = (
			'address',
			'birth_date',
			'age',
			'start_date',
			'observations',
			'phone_num',
			'photo',
			'blood_type',
			)
