from django.db import models
from django.contrib.auth.models import User

# Create your models here.

class SourceChecklist(models.Model):
    checklist_name = models.TextField()
    checklist_details = models.TextField()
    created = models.DateTimeField(auto_now_add=True)
    last_updated = models.DateTimeField(auto_now_add=True)
    owner = models.ForeignKey(User, on_delete=models.CASCADE)

class ChecklistTemplateItems(models.Model):
    template_item_short_text = models.TextField()
    template_item_long_text = models.TextField(null=True)
    sort_order = models.IntegerField(default=99)
    source_checklist = models.ForeignKey(SourceChecklist, on_delete=models.CASCADE)
    created = models.DateTimeField(auto_now_add=True)
    last_updated = models.DateTimeField(auto_now_add=True)
    ## TODO - Add repeating rules or notification rules for the checklist item.
    ##          This can be done through FK for the configuration items.
