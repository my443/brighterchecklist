# Generated by Django 4.2.3 on 2023-08-30 17:44

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('customers', '0003_customer_customer_uuid'),
    ]

    operations = [
        migrations.AlterField(
            model_name='customer',
            name='company_name',
            field=models.TextField(null=True),
        ),
    ]
