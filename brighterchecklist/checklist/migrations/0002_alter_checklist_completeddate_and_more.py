# Generated by Django 4.2.3 on 2023-07-16 11:49

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('checklist', '0001_initial'),
    ]

    operations = [
        migrations.AlterField(
            model_name='checklist',
            name='completeddate',
            field=models.DateTimeField(null=True),
        ),
        migrations.AlterField(
            model_name='checklist',
            name='startdate',
            field=models.DateTimeField(null=True),
        ),
    ]
