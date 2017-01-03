from __future__ import unicode_literals
from django.db import models
from django.conf import settings
from django.utils import timezone


class Classe_gym(models.Model):
    price_classe =  models.FloatField()
    type_classe = models.CharField(max_length=150)
    description_classe = models.CharField(max_length=200)
    

class Order_classe(models.Model):
    date_classe = models.DateTimeField(default=timezone.now)
    star_hour = models.DateTimeField(default=timezone.now)
    finish_hour = models.DateTimeField(default=timezone.now)
    orders_classe = models.ManyToManyField(Classe_gym)