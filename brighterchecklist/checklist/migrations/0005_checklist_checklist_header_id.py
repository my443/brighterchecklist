# Generated by Django 4.2.3 on 2023-08-08 00:52

from django.db import migrations, models
import django.db.models.deletion


class Migration(migrations.Migration):

    dependencies = [
        ('checklist', '0004_remove_checklist_assigned_to_user_id_and_more'),
    ]

    operations = [
        migrations.AddField(
            model_name='checklist',
            name='checklist_header_id',
            field=models.ForeignKey(default=1, on_delete=django.db.models.deletion.CASCADE, to='checklist.checklistheader'),
            preserve_default=False,
        ),
    ]
