from django.conf.urls import url
from django.contrib.auth.views import login, logout
from . import views

urlpatterns = [
	url(r'^profile/$', views.ProfileView.as_view(), name='profile'),
	url(r'^registry/$', views.RegistryView.as_view(), name='registry'),
	url(r'^registry_client/$', views.RegistryClient.as_view(), name='regclient'),
	url(r'^login/$', login, name='login'),
	url(r'^logout/$', logout,{'next_page': '/accounts/login'}, name="logout"),
	url(r'^list-client/(?P<vvalue>[-\w]+)/$', views.ListClients.as_view(), name="list-client"),
	url(r'^detail-client/(?P<id_client>\d+)$', views.DetailClient.as_view(), name="detail-client"),
	url(r'^menu/$', views.Menu.as_view(), name="menu"),
]