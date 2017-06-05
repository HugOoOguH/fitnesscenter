from __future__ import unicode_literals 
from django.db import models
from accounts.models import Client, Administrator
from django.conf import settings
# Create your models here.

class Payment(models.Model):
	client_payment = models.ForeignKey(Client, related_name="payment")
	admin = models.ForeignKey(Administrator, related_name='admin_payment')
	amount = models.FloatField()
	date_payment = models.DateField(auto_now=True)

	class Meta:
		verbose_name = "Payment"
		verbose_name_plural = "Payments"

	def __str__(self):
		return 'Pago de el cliente {}'.format(self.client_payment)

class PaymentMonthly (models.Model):
	client_monthly = models.ForeignKey(Client, related_name="paymentmonthly")
	BOOL_CHOICES = ((True, 'Pagado'), (False, 'No Pagado'))
	deadline_date = models.DateField()
	status = models.BooleanField(choices = BOOL_CHOICES, default=False)
	amount_monthly = models.FloatField()
	# missing = models.FloatField()

	class Meta:
		verbose_name = "PaymentMonthly"
		verbose_name_plural = "PaymentMonthlys"

	def __str__(self):
		return str(self.client_monthly)

	def calcular_cobro(self, pago_realizado, client_page):
		access = False
		status = False
		if client_page.status != 'PA':
			access=True
			status=True
			if pago_realizado >= self.amount_monthly:
				change = pago_realizado - self.amount_monthly
				client_page.status = 'PA'
				client_page.save()
				return (status, access, change)
			else:
				return (status, access)
		else:
			return (access, status)
					 	
	