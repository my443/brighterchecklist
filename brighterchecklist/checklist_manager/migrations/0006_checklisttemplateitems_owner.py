# Generated by Django 4.2.3 on 2023-08-15 10:25

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('checklist_manager', '0005_rename_checklisttempalteitems_checklisttemplateitems'),
    ]

    operations = [
        migrations.AddField(
            model_name='checklisttemplateitems',
            name='owner',
            field=models.IntegerField(default=1),
            preserve_default=False,
        ),
    ]
