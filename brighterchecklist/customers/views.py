import datetime

from django.shortcuts import render, redirect
from .models import Customer
from .forms import CustomerSignupForm
from .email import sendmail_simple, sendmail_by_class
from django.template import loader
from django.http import HttpResponse

def new_customer_signup(request):
    template = loader.get_template('customers/customer_details.html')

    new_customer = create_new_customer(request.POST['emailAddress'])
    form = generate_new_customer_form(new_customer)

    context = {'form': form}

    return HttpResponse(template.render(context, request))

def create_new_customer(email_address: str):
    new_customer = Customer()
    new_customer.email = email_address
    new_customer.save()

    return new_customer

def generate_new_customer_form(new_customer: Customer):
    data = {'email': new_customer.email,
            'customer_uuid': new_customer.customer_uuid}

    form = CustomerSignupForm(initial=data)

    return form

def save_customer_sign_up(request):
    customer_uuid = request.POST['customer_uuid']

    customer = Customer.objects.get(customer_uuid=customer_uuid)
    customer.company_name = request.POST['company_name']
    customer.firstname = request.POST['firstname']
    customer.lastname = request.POST['lastname']
    customer.last_updated = datetime.datetime.now()

    customer.save()

    sendmail_by_class()

    return thankyou(request)

def thankyou(request):
    template = loader.get_template('customers/thankyou.html')
    context = {}

    return HttpResponse(template.render(context, request))

def something_to_test():
    return 'hello world'


