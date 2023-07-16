from django.db import models
# from models.checklist_model import *

# Create your models here.

class Checklist(models.Model):
  source = models.CharField(max_length=255)
  startdate = models.DateTimeField(null=True)
  completeddate = models.DateTimeField(null=True)
  iscomplete = models.BooleanField(default=False)
