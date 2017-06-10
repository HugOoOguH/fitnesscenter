# -*- coding: utf-8 -*-
# Generated by Django 1.10.2 on 2017-03-24 00:23
from __future__ import unicode_literals

from django.db import migrations, models
import django.db.models.deletion


class Migration(migrations.Migration):

    initial = True

    dependencies = [
        ('accounts', '0001_initial'),
    ]

    operations = [
        migrations.CreateModel(
            name='Payment',
            fields=[
                ('id', models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('amount', models.FloatField()),
                ('date_payment', models.DateField(auto_now=True)),
                ('admin', models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, related_name='admin_payment', to='accounts.Administrator')),
                ('client_payment', models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, related_name='payment', to='accounts.Client')),
            ],
            options={
                'verbose_name_plural': 'Payments',
                'verbose_name': 'Payment',
            },
        ),
        migrations.CreateModel(
            name='PaymentMonthly',
            fields=[
                ('id', models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('deadline_date', models.DateField()),
                ('status', models.BooleanField(choices=[(True, 'Pagado'), (False, 'No Pagado')], default=False)),
                ('amount_monthly', models.FloatField()),
                ('client_monthly', models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, related_name='paymentmonthly', to='accounts.Client')),
            ],
            options={
                'verbose_name_plural': 'PaymentMonthlys',
                'verbose_name': 'PaymentMonthly',
            },
        ),
    ]