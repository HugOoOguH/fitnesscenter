from django.contrib import admin
from .models import Client, Administrator

class ClientAdmin(admin.ModelAdmin):
	raw_id_fields = ('user_client',)

class AdministratorAdmin(admin.ModelAdmin):
	raw_id_fields = ('user_administrator',)

# Register your models here.
admin.site.register(Client, ClientAdmin)
admin.site.register(Administrator, AdministratorAdmin)