from django.conf.urls import url, include
from django.contrib import admin
from django.views.static import serve
from django.conf import settings
from home import urls as urlsHome
from accounts import urls as urlsAccounts
from django.conf.urls.static import static


urlpatterns = [
    url(r'^admin/', admin.site.urls),
    url(r'^courses/',include('courses.urls', namespace="courses")),
    url(r'^accounts/', include(urlsAccounts, namespace='accounts')),
    url(r'^orders/', include('orders.urls', namespace='orders')),
    url(r'^shop/', include('shop_product.urls',namespace='shop_product')),
    url(r'^cart/', include ('cart.urls', namespace='cart')),
    url(r'^', include(urlsHome)),
    url('', include('social.apps.django_app.urls', namespace='social')),
    url(
    	regex=r'^media/(?P<path>.*)$',
    	view=serve,
    	kwargs={'document_root':settings.MEDIA_ROOT}),
    
]


if settings.DEBUG:
    urlpatterns += static(settings.MEDIA_URL,document_root= settings.MEDIA_ROOT)
