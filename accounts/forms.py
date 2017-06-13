from django import forms 
from django.contrib.auth.models import User
from .models import Administrator, Client

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
	birth_date = forms.CharField(label="Fecha de Nacimiento", widget=forms.TextInput(attrs={'class':'form-control',
		'type':'date',
		'placeholder' : 'Fecha de Nacimiento'}))
	age = forms.IntegerField(label="Edad", widget=forms.TextInput(attrs = {'class':'form-control',
		'type' : 'number',
		'placeholder' : 'Edad'}))
	# start_date = forms.CharField(label="Fecha de Inicio", widget=forms.TextInput(attrs={'class':'form-control',
	# 	'type':'date',
	# 	'placeholder' : 'Fecha de Inicio'}))
	phone_num = forms.IntegerField(label="Número Telefónico", widget=forms.TextInput(attrs = {'class':'form-control',
		'type' : 'text',
		'placeholder' : 'Numero Telefonico'}))
	blood_type = forms.CharField(label="Tipo de Sangre",widget=forms.TextInput(attrs = {'class' : 'form-control',
		'type' : 'text',
		'placeholder' : 'Tipo de sangre'}))
	address = forms.CharField(label = "Dirección", widget=forms.Textarea(attrs={'class' : 'form-control',
		'type': 'text',
		'rows' : '3',
		'placeholder' : 'Dirección'}))
	observations = forms.CharField(label="Observaciones", widget=forms.Textarea(attrs={'class' : 'form-control',
		'type' : 'text',
		'rows' : '3',
		'placeholder' : 'Observaciones'}))
	class Meta:
		model = Client
		fields = (
			'birth_date',
			'age',
			'start_date',
			'phone_num',
			'blood_type',
			'address',
			'observations',
			'photo',
			)

