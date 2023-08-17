# Generated by Django 4.2.3 on 2023-08-16 10:37

from django.conf import settings
from django.db import migrations, models
import django.db.models.deletion


class Migration(migrations.Migration):

    dependencies = [
        migrations.swappable_dependency(settings.AUTH_USER_MODEL),
        ('checklist_manager', '0007_remove_checklisttemplateitems_checklist_id_and_more'),
    ]

    operations = [
        migrations.AlterField(
            model_name='sourcechecklist',
            name='owner',
            field=models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, to=settings.AUTH_USER_MODEL),
        ),
    ]