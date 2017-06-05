from django.conf.urls import url
from . import views

urlpatterns = [
	url(r'^$', views.HomeView.as_view(), name="home"),
	url(r'^menu', views.MenuView.as_view(), name="menu_admin"),
	
]

handler404 = "views.custom_404"