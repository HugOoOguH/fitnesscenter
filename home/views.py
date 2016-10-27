from django.shortcuts import render
from django.views.generic import View
# Create your views here.
class HomeView(View):
	def get(self,request):
		template_name = "home/home.html"
		context = {}
		return render(request, template_name, context)