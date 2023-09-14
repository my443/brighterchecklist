# Generated by Django 4.2.3 on 2023-09-14 09:41

import datetime
from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('customers', '0007_customer_account_expiry_date'),
    ]

    operations = [
        migrations.RemoveField(
            model_name='customer',
            name='days_until_account_expiry',
        ),
        migrations.AlterField(
            model_name='customer',
            name='account_expiry_date',
            field=models.DateField(default=datetime.datetime(2023, 9, 29, 5, 41, 22, 128685)),
        ),
    ]