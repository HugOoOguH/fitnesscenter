from django.shortcuts import render
from django.views.generic import View
from accounts.models import Client, Administrator

# Create your views here.
class HomeView(View):
	def get(self,request):
		template_name = "home/home.html"
		context = {}
		return render(request, template_name, context)
	

class MenuView(View):
	def get(self,request):
		template_name = "menu_admin/menu.html"
		context = {}
		return render(request,template_name, context)


def custom_404(request):
    return  render(request,'404.html')	