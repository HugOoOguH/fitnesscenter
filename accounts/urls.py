from django.conf.urls import url
from django.contrib.auth.views import login, logout, logout_then_login, password_change, password_change_done, password_reset,password_reset_done, password_reset_confirm, password_reset_complete
from . import views
from django.core.urlresolvers import reverse

urlpatterns = [
	# url('^', include('django.contrib.auth.urls')),
	#url destinada para el administrador de el sitio
	url(r'^profile/$', views.ProfileView.as_view(), name='profile'),
	#url destinada para loguear a los usuarios administradores
	url(r'^login/$', login, name='login'),
	#url destinada para cerrar sesion de usuarios
	url(r'^logout/$', logout, name="logout"),
	# url(r'^logout/$', logout,{'next_page': '/accounts/login'}, name="logout"),
	
	url(r'^logout-then-login/$', logout_then_login, name="logout-then-login"),

	#url para cambiar la contraseña de el usuario
	url(r'^password-change/$', password_change, {'post_change_redirect':'accounts:password_change_done'}, name="password_change"),
	url(r'^password-change/done/$', password_change_done, name="password_change_done"),

	#urls para restaurar la contraseña
	url(r'^password-reset/$', password_reset,{'post_reset_redirect':'accounts:password_reset_done'}, name="password_reset"),
	url(r'^password-reset/done/$', password_reset_done, name="password_reset_done"),
	url(r'^password-reset/confirm/(?P<uidb64>[-\w]+)/(?P<token>[-\w]+)/$', password_reset_confirm, {'post_reset_redirect':'accounts:password_reset_complete'}, name="password_reset_confirm"),
	url(r'^password-reset/complete/$', password_reset_complete, name="password_reset_complete"),

	#url destinada para el registro de administradores
	url(r'^registry/$', views.RegistryView.as_view(), name='registry'),
	url(r'^registry-complete', views.RegistryCompleteView.as_view(), name="registry-complete"),
	
	#url destinada para el registro de clientes
	url(r'^registry_client/$', views.RegistryClient.as_view(), name='regclient'),
	
	#url destinada a enlistar todos los clientes de el gimnasio
	url(r'^list-client/$', views.ListClients.as_view(), name="list-client"),
	#url destianada para mostrar una lista de clientes filtrados
	url(r'^list-client/(?P<vvalue>[-\w]+)/$', views.ListClients.as_view(), name="list-client-filter"),
	
	#url que sirve para mostrar la vista detalle de cada cliente
	url(r'^detail-client/(?P<id_client>\d+)/$', views.DetailClient.as_view(), name="detail-client"),
	# url(r'^client-detail/(?P<ide>\d+)/'),

	#Eliminar menu
	# url(r'^menu/$', views.Menu.as_view(), name="menu"),
]

