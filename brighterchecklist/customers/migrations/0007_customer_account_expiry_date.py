# Generated by Django 4.2.3 on 2023-09-14 09:39

import datetime
from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('customers', '0006_customer_days_until_account_expiry'),
    ]

    operations = [
        migrations.AddField(
            model_name='customer',
            name='account_expiry_date',
            field=models.DateField(default=datetime.datetime(2023, 9, 29, 5, 39, 53, 503219)),
        ),
    ]