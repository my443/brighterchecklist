from django.db import models

# Create your models here.

class SourceChecklist(models.Model):
    checklist_name = models.TextField()
    checklist_details = models.TextField()
    created = models.DateTimeField(auto_now_add=True)
    last_updated = models.DateTimeField(auto_now_add=True)
    owner = models.IntegerField()
