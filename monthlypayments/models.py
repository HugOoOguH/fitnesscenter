from __future__ import unicode_literals 
from django.db import models
from accounts.models import Client, Administrator
from django.conf import settings

# Create your models here.

class DeadlineManager(models.Manager):
	def get_queryset(self):
		return super(DeadlineManager, self).get_queryset().filter(status=False)



class PriceMonth(models.Model):

	BOOL_CHOICES = ((True, 'Active'), (False, 'Inactive'))
	price = models.IntegerField()
	available = models.BooleanField(choices = BOOL_CHOICES, default = True)


class PaymentMonthly (models.Model):
	BOOL_CHOICES = ((True, 'Pagado'), (False, 'No Pagado'))
	client_monthly = models.ForeignKey(Client, related_name="paymentmonthly")
	deadline_date = models.DateField()
	status = models.BooleanField(choices = BOOL_CHOICES, default=False)
	##Quitar de aqui
	# amount_monthly = models.FloatField()
	objects = models.Manager()
	deadline = DeadlineManager()
	# missing = models.FloatField()

	class Meta:
		verbose_name = "PaymentMonthly"
		verbose_name_plural = "PaymentMonthlys"

	def __str__(self):
		return str(self.client_monthly.user_client.first_name)

	# def calcular_cobro(self, pago_realizado, client_page):
	# 	access = False
	# 	status = False
	# 	if client_page.status != 'PA':
	# 		access=True
	# 		status=True
	# 		if pago_realizado >= self.amount_monthly:
	# 			change = pago_realizado - self.amount_monthly
	# 			client_page.status = 'PA'
	# 			client_page.save()
	# 			return (status, access, change)
	# 		else:
	# 			return (status, access)
	# 	else:
	# 		return (access, status)
					 	
	
class Payment(models.Model):
	monthly_payment = models.ForeignKey(PaymentMonthly, related_name="payment")
	admin = models.ForeignKey(Administrator, related_name='admin_payment')
	amount = models.FloatField()
	date_payment = models.DateField(auto_now=True)

	class Meta:
		verbose_name = "Payment"
		verbose_name_plural = "Payments"

	def __str__(self):
		return 'Pago de el cliente {}'.format(self.monthly_payment)

