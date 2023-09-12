# Generated by Django 4.2.3 on 2023-09-12 10:14

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('customers', '0004_alter_customer_company_name'),
    ]

    operations = [
        migrations.AddField(
            model_name='customer',
            name='customer_type',
            field=models.TextField(choices=[('CM', 'Checklist Manager'), ('CC', 'Checklist Completer')], default='CM', max_length=2),
        ),
    ]
