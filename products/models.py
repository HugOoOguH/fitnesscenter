from __future__ import unicode_literals
from django.db import models
from django.conf import settings
from django.utils import timezone


# Create your models here.
class Product(models.Model):
			name = models.CharField(max_length=150)
			presentation = models.CharField(max_length=100)
			stock = models.IntegerField()
			price = models.FloatField()
			


class Order_product(models.Model):
			date_order = models.DateTimeField(default=timezone.now)
			total_order = models.FloatField()
			Orders_product = models.ManyToManyField(Product)

	