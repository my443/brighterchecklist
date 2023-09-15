import datetime

from django.shortcuts import render, redirect
from django.db.models import DEFERRED                   ## Used to get the _state of a transaction
from django.contrib.auth.models import User
from django.template import loader
from django.http import HttpResponse
from django.contrib import messages

from .models import Customer
from .forms import CustomerForm
from .email import sendmail_simple, sendmail_by_class, sendemail_with_template
import shared.random_password_generator as random_password_generator

def edit_customer(request, id):
    """For when a Checklist Manager adds a customer"""

    template = loader.get_template('customers/customer_details_in_app.html')

    customer = get_customer_details(request, id)
    save_customer_details(request, id, customer)

    form = generate_customer_form(customer)

    days_until_expiry = get_days_until_expiry(customer.account_expiry_date)

    context = {'customer': customer,
               'form': form,
               'days_until_expiry': days_until_expiry}

    return HttpResponse(template.render(context, request))

def get_customer_details(request, id):
    if id == 0:
        customer = Customer()
        customer.account_expiry_date = datetime.date.today() + datetime.timedelta(days=15)
    else:
        customer = Customer.objects.get(id=id)

    return customer

def get_days_until_expiry(expiry_date):
    days_until_expiry = (expiry_date - datetime.date.today()).days
    return days_until_expiry

def save_customer_details(request, id, customer):
    if request.method == "POST":
        form = CustomerForm(request.POST)
        if form.is_valid():
            customer.firstname = form.cleaned_data['firstname']
            customer.lastname = form.cleaned_data['lastname']
            customer.customer_type = form.cleaned_data['customer_type']
            customer.customer_uuid = form.cleaned_data['customer_uuid']
            customer.email = form.cleaned_data['email']
            customer.company_name = form.cleaned_data['company_name']

            ## TODO - Start here.
            ## Add that if the email doesn't exist, add the customer.
            ## Then add the relationship
            ## Otherwise you just save the customer.
            if Customer.objects.filter(email=customer.email).exists():
                messages.error(request, 'That item already exists')

            # if customer._state.adding:
            #     add_user(customer.firstname, customer.lastname, customer.email)
            else:
                customer.save()

            return True                     ## True if the form is saved.
        else:
            return False                    ## False if form is not saved. This could just be because it wasn't a POST


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

def list_customers(request):
    template = loader.get_template('customers/customer_list.html')
    customers = Customer.objects.all().order_by('id')

    context = { 'customers': customers }

    return HttpResponse(template.render(context, request))

def add_user(firstname, lastname, email):
    """Adds a new user when needed.
        Also updates the user/customer relationship."""

    password = random_password_generator.random_password(12)

    user = User.objects.create_user(username=email, first_name=firstname, last_name=lastname, password=password)
    user.save()

    return user.id

def add_customer_to_user_connection(user_id, customer_id):
    pass
