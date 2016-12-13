from django.contrib import admin
from .models import Payment, PaymentMonthly

# Register your models here.
admin.site.register(Payment)
admin.site.register(PaymentMonthly)