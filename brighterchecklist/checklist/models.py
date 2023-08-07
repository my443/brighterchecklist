from django.db import models
# from models.checklist_model import *

# Create your models here.

class Checklist(models.Model):
  checklist_item_short_text = models.TextField()
  checklist_item_long_text = models.TextField()
  startdate = models.DateTimeField(null=True)
  checklist_item_users_notes = models.TextField()
  sort_order = models.IntegerField(default=99)
  checklist_id = models.IntegerField()
  assigned_to_user_id = models.IntegerField()
  completeddate = models.DateTimeField(null=True)
  iscomplete = models.BooleanField(default=False)