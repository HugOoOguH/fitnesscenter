from django.shortcuts import render, redirect
from django.views.generic import View
from .forms import UserRegistrationForm
from django.contrib.auth.models import User
from django.utils.decorators  import method_decorator
from django.contrib.auth.decorators import login_required
from .models import Administrator

class RegistryView(View):
	@method_decorator(login_required)
	def get(self, request):
		template_name = "registration/registry_admin.html";	
		form = UserRegistrationForm()
		context = {
			'form' : form,
		}
		return render(request, template_name, context)

	def post(self, request):
		template_name = "registration/registry_admin.html"
		new_user_f = UserRegistrationForm(request.POST)
		if new_user_f.is_valid():
			new_user = new_user_f.save(commit=False)
			new_user.set_password(new_user_f.cleaned_data['password'])
			new_user.save()
			admin = Administrator()
			admin.user_administrator = new_user
			admin.save()
			return redirect('home')
		else:
			context = {
				'form':new_user_f,
			}
			return render (request, template_name, context)

class ProfileView(View):
	pass