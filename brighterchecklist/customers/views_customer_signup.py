import datetime

from django.contrib.auth.models import User
from .models import Customer, UsersToCustomerRelationship
from .forms import CustomerSignupForm
from .email import sendemail_with_template
from django.template import loader
from django.http import HttpResponse
import shared.random_password_generator as random_password_generator
from django.shortcuts import redirect
from django.contrib import messages


def new_customer_signup(request) -> HttpResponse:
    template = loader.get_template('customers/customer_details.html')

    if customer_already_exists(request):
        return redirect('home')

    new_customer = create_new_customer(request.POST['emailAddress'])
    form = generate_new_customer_form(new_customer)

    context = {'form': form}

    return HttpResponse(template.render(context, request))

def create_new_customer(email_address: str) -> Customer:
    new_customer = Customer()
    new_customer.email = email_address
    new_customer.save()

    return new_customer

def customer_already_exists(request)-> bool:
    """Find out if that email address already exists"""
    if Customer.objects.filter(email=request.POST['emailAddress']).exists():
        messages.error(request,
                       'That email address already exists in our system.<br>Every account requires a unique email address.')
        return True
    else:
        return False

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

    user = create_new_user_for_new_customers(customer.email)
    add_new_customer_to_user_connection(user, customer)

    send_email_after_save(customer, user.password)

    return thankyou(request)

def send_email_after_save(customer, password):
    context = { 'customer': customer,
                'password': password}
    sendemail_with_template(customer.email, context)

    return 0

def thankyou(request):
    template = loader.get_template('customers/thankyou.html')
    context = {}

    return HttpResponse(template.render(context, request))


def something_to_test():
    return 'hello world'

def create_new_user_for_new_customers(email):
    """Adds a new user when needed.
        Also updates the user/customer relationship."""

    password = random_password_generator.random_password(12)

    user = User.objects.create_user(username=email, password=password)
    user.save()

    user.password = password

    return user

def add_new_customer_to_user_connection(user: User, customer: Customer) -> bool:
    """Used for NEW customers."""

    manager = User.objects.get(pk=1)
    relationship = UsersToCustomerRelationship()

    relationship.user = user
    relationship.customer = customer
    relationship.manager = user
    relationship.is_active = True

    relationship.save()

    return True
