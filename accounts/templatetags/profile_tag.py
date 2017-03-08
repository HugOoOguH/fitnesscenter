from django import template
register = template.Library()
from django.contrib.auth.models import User
from ..models import Client, Administrator

@register.simple_tag
def image_user_admin():
    adm = Administrator.objects.all()
    return adm