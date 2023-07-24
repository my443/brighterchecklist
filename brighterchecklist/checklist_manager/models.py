from django.db import models

# Create your models here.

class SourceChecklist(models.Model):
    checklist_name = None
    checklist_details = None
    created = ''
    last_updated = ''
    owner = ''
