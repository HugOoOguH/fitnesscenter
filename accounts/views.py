from django.shortcuts import render, redirect
from django.views.generic import View
from .forms import UserRegistrationForm, AdminForm
from django.contrib.auth.models import User
from django.utils.decorators  import method_decorator
from django.contrib.auth.decorators import login_required, user_passes_test
from .models import Administrator

class RegistryView(View):
	@method_decorator(login_required)
	# @staff_member_required
	# @method_decorator(staff_member_required)
	def get(self, request):

		template_name = "registration/registry_admin.html";	
		form = UserRegistrationForm()
		form_adm = AdminForm()
		context = {
			'form' : form,
			'form_adm' : form_adm,
		}
		return render(request, template_name, context)

	def post(self, request):
		template_name = "registration/registry_admin.html"
		new_user_f = UserRegistrationForm(request.POST)
		new_admin_f = AdminForm(request.POST)
		if new_user_f.is_valid() and new_admin_f.is_valid():
			new_user = new_user_f.save(commit=False)
			new_admin = new_admin_f.save(commit=False) 
			new_user.set_password(new_user_f.cleaned_data['password'])
			new_user.save()
			new_admin.user_administrator = new_user
			# admin = Administrator()
			# admin.user_administrator = new_user
			new_admin.save()
			return redirect('home')
		else:
			context = {
				'form':new_user_f,
			}
			return render (request, template_name, context)

# def class RegistryClient(View):
# 	template_name = "registration/registry_client.html"
# 	form 

class ProfileView(View):
	pass