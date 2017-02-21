from django.db import models
from datetime import datetime

class Course(models.Model):
    name = models.CharField(max_length=140)
    price =models.DecimalField(max_digits=10, decimal_places=2)
    start_date = models.DateTimeField(default=datetime.now, blank=True)
    picture = models.ImageField(upload_to='media/courses/pictures', blank=True)
    available = models.BooleanField(default = True)