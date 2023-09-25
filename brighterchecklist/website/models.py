from django.db import models
from django.contrib.auth.models import User
import datetime

class Feedback(models.Model):
    feedback_text = models.TextField(null=True)
    user_giving_feedback = models.ForeignKey(settings.AUTH_USER_MODEL, related_name='user_giving_feedback', null=True)
    feedback_date_time = models.DateTimeField(default=datetime.datetime.now())
