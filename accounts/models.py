from __future__ import unicode_literals 
from django.db import models
from django.contrib.auth.models import User
from django.conf import settings
from datetime import datetime
import uuid

# Create your models here.
class Client(models.Model):
	STATUS_CLIENT = (
		('PA', 'Pagado'),
		('PE', 'Pendiente'),
		('AT', 'Atrasado'), 
		)
	user_client = models.OneToOneField(settings.AUTH_USER_MODEL, blank=True, null=True)
	unique_id = models.UUIDField(primary_key=True, default=uuid.uuid4, editable=False)
	address = models.CharField(max_length=200)
	birth_date = models.DateField(default=datetime.now, blank=True)
	age = models.IntegerField()
	start_date = models.DateField(default=datetime.now, blank=True)
	observations = models.TextField()
	phone_num = models.CharField(max_length=30)
	photo = models.ImageField(upload_to="clients", blank=True, null=True)
	blood_type = models.CharField(max_length=50)
	status = models.CharField(max_length=2, choices=STATUS_CLIENT, blank=True, null=True)

	class Meta:
		verbose_name = "Client"
		verbose_name_plural = "Clients"

	def __str__(self):
		return 'Cliente {}'.format(self.user_client)

class Administrator(models.Model):
	user_administrator = models.OneToOneField(settings.AUTH_USER_MODEL)
	BOOL_CHOICES = ((True, 'Si'), (False, 'No'))
	photo = models.ImageField(upload_to="administrators", blank=True, null=True)
	administrator_root =  models.BooleanField(choices = BOOL_CHOICES, default=False)
	
	class Meta:
		verbose_name = "Administrator"
		verbose_name_plural = "Administrators"

	def __str__(self):
		return 'Administrador {}'.format(self.user_administrator)