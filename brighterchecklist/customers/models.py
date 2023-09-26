from django.db import models
from django.contrib.auth.models import User
from django.conf import settings
import uuid
import datetime

FUTURE_DATE = datetime.datetime.now() + datetime.timedelta(days=15)

class Customer(models.Model):
    CUSTOMER_TYPE = [
        ("CM", "Checklist Manager"),
        ("CC", "Checklist Completer"),
    ]
    company_name = models.TextField(null=True)                       ## If no company name is supplied, the feild is the first-lastname feilds.
    firstname = models.TextField(null=True)
    lastname = models.TextField(null=True)
    email = models.TextField(null=True, unique=True)
    customer_type = models.TextField(max_length=2, choices=CUSTOMER_TYPE, default="CM")
    customer_uuid = models.UUIDField(default = uuid.uuid4, editable = False, null=False)
    account_expiry_date = models.DateField(default=FUTURE_DATE)
    created = models.DateTimeField(auto_now_add=True)
    last_updated = models.DateTimeField(auto_now_add=True)

class UsersToCustomerRelationship(models.Model):
    customer = models.OneToOneField("Customer", on_delete=models.PROTECT, related_name='customer')
    user = models.OneToOneField(settings.AUTH_USER_MODEL, on_delete=models.PROTECT, related_name='user')
    manager = models.ForeignKey(settings.AUTH_USER_MODEL, on_delete=models.PROTECT, related_name='manager')
    created = models.DateTimeField(auto_now_add=True)
    last_updated = models.DateTimeField(auto_now_add=True)
    is_active = models.BooleanField()

