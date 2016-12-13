from django.db import models
from django.utils import timezone


# Create your models here.
class type_visit(models.Model):
            price_visit = models.FloatField()
            creation_visit = models.DateTimeField(default=timezone.now)
            type_visit = models.CharField(max_length=200)
            description_visit = models.CharField(max_length=200)

class Order_visit(models.Model):
            date_visit = models.DateTimeField()
            star_hour = models.fields.DateTimeField()
            finish_visit = models.fields.DateTimeField()
            Orders_visit = models.ManyToManyField(type_visit)
