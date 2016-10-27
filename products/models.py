from __future__ import unicode_literals
from django.db import models
from django.conf import settings

# Create your models here.
class Product(models.Model):
	name = models.CharField(max_length=150)
	presentation = models.CharField(max_length=100)
	availability = models.IntegerField()
	price = models.FloatField()

	