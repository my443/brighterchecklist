# Generated by Django 4.2.3 on 2023-09-17 11:00

import datetime
from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('customers', '0009_alter_customer_account_expiry_date_and_more'),
    ]

    operations = [
        migrations.AlterField(
            model_name='customer',
            name='account_expiry_date',
            field=models.DateField(default=datetime.datetime(2023, 10, 2, 7, 0, 18, 561778)),
        ),
    ]
