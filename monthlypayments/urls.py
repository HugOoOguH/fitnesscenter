from django.conf.urls import url
from . import views

urlpatterns = [
	#Url para el pago de clientes
	url(r'page/(?P<id>[-\w]+)/(?P<correct>\d+)/$', views.PageClient.as_view(), name='page-client'),
	url(r'payment-complete/(?P<result>\d+)/$', views.PayComplete.as_view(), name='payment-complete'),
	# url(r'page/(?P<id>[-\w]+)/(?P<correct>\d+)/$', views.PageClient.as_view(), name='page-client-incorrect'),
]