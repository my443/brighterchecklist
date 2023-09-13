import datetime

from django.shortcuts import render, redirect
from .models import Customer
from .forms import CustomerForm
from .email import sendmail_simple, sendmail_by_class, sendemail_with_template
from django.template import loader
from django.http import HttpResponse

def add_customer(request):
    """For when a Checklist Manager adds a customer"""

    template = loader.get_template('customers/customer_details_in_app.html')
    customer = Customer.objects.get(id=129)
    form = generate_customer_form(customer)

    context = {'customer': customer,
               'form': form}

    return HttpResponse(template.render(context, request))

def generate_customer_form(customer: Customer):

    data = {
        'company_name': customer.company_name,
        'firstname': customer.firstname,
        'lastname': customer.lastname,
        'email': customer.email,
        'customer_type': customer.customer_type,
        'customer_uuid': customer.customer_uuid
    }

    form = CustomerForm(initial=data)

    return  form