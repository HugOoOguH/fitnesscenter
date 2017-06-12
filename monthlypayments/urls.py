from django.conf.urls import url
from . import views

urlpatterns = [
	#Url para el pago de clientes
	url(r'page/(?P<id>[-\w]+)/$', views.PageClient.as_view(), name='page-client'),
]