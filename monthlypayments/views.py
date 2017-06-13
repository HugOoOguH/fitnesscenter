from django.shortcuts import render, get_object_or_404, redirect
from django.views.generic import View
from django.contrib.auth.models import User
from accounts.models import Client, Administrator
from .forms import PageClientForm
from .models import Payment, PaymentMonthly, PriceMonth
from .AssignDate import AssignDate

# Create your views here.
class PageClient(View):
	def get(self, request, id, correct):
		if correct:
			correct = True
		else:
			correct = False
		access = False
		template_name = "monthlypayments/pago.html"
		price = get_object_or_404(PriceMonth, available=True)
		cliente = get_object_or_404(Client, unique_id=id)
		if cliente.status == 'PA':
			access = True
		form = PageClientForm()
		context = {
			'access':access,
			'price':price.price,
			'cliente':cliente,
			'form': form,
			'correct':correct,
		}
		return render(request, template_name, context)


	def post(self, request, id, correct):
		template_name = "monthlypayments/pago.html"
		if correct:
			correct = True
		else:
			correct = False
		access = False
		price = get_object_or_404(PriceMonth, available=True)
		admini = get_object_or_404(Administrator, user_administrator=request.user)
		cliente = get_object_or_404(Client, unique_id = id)
		if cliente.status == 'PA':
			access = True
		month_debt = get_object_or_404(PaymentMonthly, client_monthly = cliente, status = False)
		form = PageClientForm(request.POST)
		if form.is_valid():
			pago = form.cleaned_data
			monto = pago['pagofield']
			if monto < price.price:
				return redirect('monthlypayments:page-client', id = cliente.unique_id, correct = 0)
			result = monto - price.price
			#
			cliente.status = 'PA'
			cliente.save()
			#
			month_debt.status = True
			month_debt.save()
			#
			payment = Payment()
			payment.monthly_payment = month_debt
			payment.admin = admini
			payment.amount = price.price
			payment.save()
			#
			new_date = AssignDate(month_debt.deadline_date)
			new_date.asignar_fecha()

			new_debt = PaymentMonthly()
			new_debt.client_monthly = cliente
			new_debt.deadline_date = new_date.fecha
			new_debt.save()

			return redirect('monthlypayments:payment-complete', result = result)

		else:
			form = PageClientForm()
			context = {
				'access':access,
				'price':price.price,
				'cliente':cliente,
				'form': form,
				'correct':correct,
			}
			return render(request, template_name, context)


class PayComplete(View):
	def get(self, request, result):
		if result == 0:
			cambio = False
		else:
			cambio = True
		template_name = 'monthlypayments/complete.html'
		context = {
			'result':result,
			'cambio':cambio,
		}
		return render(request, template_name, context)





		# #Template de page client
		# template_name = "monthlypayments/pago.html"
		# #Obtener el cliente en base a su unique_id que se declaro aqui en models.py
		# cliente = get_object_or_404(Client, unique_id=id)
		# #Instanciar formulario de la app monthlypayments con la data que se envia de la vista
		# form = PageClientForm(request.POST)
		# #Verificar si la información en el formulario es valida
		# if form.is_valid():
		# 	#Se baja al administrador que en ese momento esta ejecutando la tansaccion
		# 	admini = get_object_or_404(Administrator, user_administrator=request.user)
		# 	#Instanciar la información de el formulario
		# 	pago = form.cleaned_data
		# 	#Obtener la información y estatus de pago de el cliente
		# 	paymonth = get_object_or_404(PaymentMonthly, client_monthly=cliente)
		# 	#realizar la operación de cobro

		# 	pago_realizado = pago['pagofield']
		# 	result = paymonth.calcular_cobro(pago_realizado, cliente)
		# 	print(result)

		# 	#Registrar el pago de el cliente
		# 	#Instancia de el modelo Payment
		# 	payment = Payment()
		# 	#Se asigna un cliente
		# 	payment.client_payment = cliente
		# 	#Se asigna el monto de su pago
		# 	payment.amount = paymonth.amount_monthly
		# 	#Se aasigna el administrador en turno
		# 	payment.admin = admini
		# 	#Se gruada la informacion
		# 	payment.save()
		# 	#Una vez guardado el objeto redireccionamos
		# 	# al perfil de el usuario al que cobramos		
		# 	return redirect('accounts:detail-client', id_client=cliente.user_client_id)
		# #Si la informacion no es valida que simplemente haga una instancia de el formulario
		# else:
		# 	#instanciamos el formulario
		# 	form = PageClientForm()
		# context = {
		# 	##Mandamos el cliente y el formulario nuevamente para renderizarlos en la vista 
		# 	#PagoClient()
		# 	'cliente':cliente,
		# 	'form':form,
		# }

		# return render(request, template_name, context)
		


