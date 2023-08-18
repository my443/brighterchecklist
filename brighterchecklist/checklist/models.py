from django.db import models
from checklist_manager.models import SourceChecklist

# from models.checklist_model import *

# Create your models here.

class Checklist(models.Model):
  checklist_item_short_text = models.TextField()
  checklist_item_long_text = models.TextField()
  startdate = models.DateTimeField(null=True)
  checklist_item_users_notes = models.TextField()
  sort_order = models.IntegerField(default=99)
  checklist_header = models.ForeignKey("ChecklistHeader", on_delete=models.CASCADE)
  # checklist_id = models.IntegerField()
  # assigned_to_user_id = models.IntegerField()
  completeddate = models.DateTimeField(null=True)
  iscomplete = models.BooleanField(default=False)

class ChecklistHeader(models.Model):
  source_checklist = models.ForeignKey(SourceChecklist, on_delete=models.CASCADE)
  assigned_to_user_id = models.IntegerField()
  checklist_custom_title = models.TextField()
  checklist_notes = models.TextField()
  checklist_startdate = models.DateTimeField(null=True)
  checklist_completed_date = models.DateTimeField(null=True)
  checklist_iscomplete = models.BooleanField(default=False)
