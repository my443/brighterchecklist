from django.db import models
from django.contrib.auth.models import User
from django.conf import settings
import datetime

class Feedback(models.Model):
    feedback_text = models.TextField(null=True)
    user_giving_feedback = models.ForeignKey(settings.AUTH_USER_MODEL, on_delete=models.DO_NOTHING, related_name='user_giving_feedback', null=True)
    feedback_date_time = models.DateTimeField(default=datetime.datetime.now)
