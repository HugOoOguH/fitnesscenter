from django.conf.urls import url
from . import views

urlpatterns = [
	url(r'page/(?P<id>[-\w]+)/$', views.PageClient.as_view(), name='page-client'),
]