# Generated by Django 4.2.3 on 2023-08-30 15:18

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('customers', '0001_initial'),
    ]

    operations = [
        migrations.AddField(
            model_name='customer',
            name='email',
            field=models.TextField(null=True),
        ),
    ]