# Generated by Django 4.2.3 on 2023-08-08 00:54

from django.db import migrations


class Migration(migrations.Migration):

    dependencies = [
        ('checklist', '0005_checklist_checklist_header_id'),
    ]

    operations = [
        migrations.RenameField(
            model_name='checklist',
            old_name='checklist_header_id',
            new_name='checklist_header',
        ),
    ]