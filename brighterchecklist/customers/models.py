from django.db import models
from django.contrib.auth.models import User
from django.conf import settings

class Customer(models.Model):
    company_name = models.TextField()                       ## If no company name is supplied, the feild is the first-lastname feilds.
    firstname = models.TextField(null=True)
    lastname = models.TextField(null=True)
    email = models.TextField(null=True)
    created = models.DateTimeField(auto_now_add=True)
    last_updated = models.DateTimeField(auto_now_add=True)

class UsersToCustomerRelationship(models.Model):
    customer = models.ForeignKey("Customer", on_delete=models.PROTECT)
    user = models.ForeignKey(settings.AUTH_USER_MODEL, on_delete=models.PROTECT)
    created = models.DateTimeField(auto_now_add=True)
    last_updated = models.DateTimeField(auto_now_add=True)
    is_active = models.BooleanField()

