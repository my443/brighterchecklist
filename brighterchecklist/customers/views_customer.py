import datetime

from django.shortcuts import render, redirect
from .models import Customer
from .forms import CustomerSignupForm, ProfileUpdateForm
from .email import sendmail_simple, sendmail_by_class, sendemail_with_template
from django.template import loader
from django.http import HttpResponse

def add_customer(request):
    """For when a Checklist Manager adds a customer"""

    template = loader.get_template('customers/customer_details_in_app.html')
    customer = Customer.objects.get(id=129)

    context = {'customer': customer}

    return HttpResponse(template.render(context, request))