from django.contrib import admin
from .models import Course

# Register your models here.

class CourseAdmin(admin.ModelAdmin):
    list_display = ['name', 'price','start_date','picture']
    list_filter = ['available']
admin.site.register(Course, CourseAdmin)
