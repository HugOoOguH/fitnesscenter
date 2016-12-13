from django.contrib import admin
from .models import Client, Administrator


# Register your models here.
admin.site.register(Client)
admin.site.register(Administrator)