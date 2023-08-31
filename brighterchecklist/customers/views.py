import datetime

from django.shortcuts import render, redirect
from .models import Customer
from .forms import CustomerSignupForm
from django.template import loader
from django.http import HttpResponse

def new_customer_signup(request):
    template = loader.get_template('customers/customer_details.html')

    new_customer = Customer()
    new_customer.email = request.POST['emailAddress']
    new_customer.save()

    data = {'email': new_customer.email,
            'customer_uuid': new_customer.customer_uuid}

    form = CustomerSignupForm(initial=data)

    context = {'form': form}

    return HttpResponse(template.render(context, request))

def save_customer_sign_up(request):
    customer_uuid = request.POST['customer_uuid']

    customer = Customer.objects.get(customer_uuid=customer_uuid)
    customer.company_name = request.POST['company_name']
    customer.firstname = request.POST['firstname']
    customer.lastname = request.POST['lastname']
    customer.last_updated = datetime.datetime.now()

    customer.save()

    return thankyou(request)

def thankyou(request):
    template = loader.get_template('customers/thankyou.html')
    context = {}

    return HttpResponse(template.render(context, request))


