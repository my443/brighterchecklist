import datetime

from django.contrib.auth.models import User
from .models import Customer, UsersToCustomerRelationship
import shared.random_password_generator as random_password_generator
from django.shortcuts import redirect
from django.contrib import messages
from .views_customer import add_user, add_customer_to_user_connection, send_welcome_email


def new_customer_signup(request):

    if customer_already_exists(request):
        return redirect('home')

    password = random_password_generator.random_password(15)

    customer = create_new_customer(request.POST['emailAddress'])

    user = add_user("<No Firstname Given>", "<No Lastname Given>", customer.email, password)
    ## For your first sign-up, the user is the manager.
    manager = user
    add_customer_to_user_connection(user, customer, manager)
    send_welcome_email(customer, password)

    messages.success(request, """<h3>You are all set!</h3>
                                        Check your email for your username and password.
                                        <br>You have full access to all of BrighterChecklist for 15 days! 
                                        <br><b><i>For Free.</i></b>""")

    return redirect('home')

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

