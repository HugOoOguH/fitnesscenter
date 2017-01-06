from django import forms 
from django.contrib.auth.models import User
from .models import Administrator

class UserRegistrationForm(forms.ModelForm):
	username = forms.CharField(label="",widget=forms.TextInput(attrs={'class' : 'form_login', 'placeholder':"Nombre usuario"	}))
	email = forms.CharField(label="", widget=forms.TextInput(attrs={'class':'form_login', 'placeholder':"Correo electronico"}))
	password = forms.CharField(label="",widget=forms.PasswordInput(attrs={'placeholder':'contraseña'}))
	password2 = forms.CharField(label="",widget=forms.PasswordInput(attrs={'placeholder':'Repite contraseña'}))


	class Meta:
		model = User;
		fields = ('username', 'email')
		help_texts = {
			'username' : None,
		}


	def clean_password2(self):
		clean = self.cleaned_data
		if clean['password']!= clean['password2']:
			raise forms.ValidationError("Las contraseñas no coinciden")
		return clean['password2']

class AdminForm(forms.ModelForm):
	class Meta:
		model = Administrator
		fields = (
			'administrator_root',
			) 