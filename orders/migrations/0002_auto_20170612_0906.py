# -*- coding: utf-8 -*-
# Generated by Django 1.10.2 on 2017-06-12 14:06
from __future__ import unicode_literals

from django.db import migrations, models
import django.db.models.deletion


class Migration(migrations.Migration):

    dependencies = [
        ('accounts', '0003_auto_20170606_2306'),
        ('orders', '0001_initial'),
    ]

    operations = [
        migrations.RemoveField(
            model_name='order',
            name='user_name',
        ),
        migrations.AddField(
            model_name='order',
            name='user_administrator',
            field=models.ForeignKey(default=0.0004957858205255329, on_delete=django.db.models.deletion.CASCADE, related_name='user_administrators', to='accounts.Administrator'),
            preserve_default=False,
        ),
    ]
