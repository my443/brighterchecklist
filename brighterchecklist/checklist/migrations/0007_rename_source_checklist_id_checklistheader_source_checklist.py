# Generated by Django 4.2.3 on 2023-08-17 10:48

from django.db import migrations


class Migration(migrations.Migration):

    dependencies = [
        ('checklist', '0006_rename_checklist_header_id_checklist_checklist_header'),
    ]

    operations = [
        migrations.RenameField(
            model_name='checklistheader',
            old_name='source_checklist_id',
            new_name='source_checklist',
        ),
    ]
