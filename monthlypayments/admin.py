from django.contrib import admin
from .models import Payment, PaymentMonthly, PriceMonth

# Register your models here.
admin.site.register(Payment)
admin.site.register(PaymentMonthly)
admin.site.register(PriceMonth)
