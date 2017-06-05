from django import forms 
from django.contrib.auth.models import User
from .models import Payment, PaymentMonthly


class PageClientForm(forms.Form):
	pagofield = forms.IntegerField(label="Monto del cliente", widget=forms.TextInput(attrs={'class' : 'form-control', 
      'type' : 'number', 
      'placeholder' : 'Monto de el cliente'}))

