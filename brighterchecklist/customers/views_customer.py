import datetime


from django.shortcuts import redirect
from django.contrib.auth.models import User
from django.template import loader
from django.http import HttpResponse
from django.contrib import messages

from .models import Customer, UsersToCustomerRelationship
from .forms import CustomerForm
from .email import sendemail_with_template
import shared.random_password_generator as random_password_generator
from .views_customer_helpers import get_days_until_expiry
import urllib.parse

## STRIPE_URL = 'https://buy.stripe.com/fZe4iq03Y7NT0FOaEE'                 ## Live
STRIPE_URL = 'https://buy.stripe.com/test_14k7wo7uRe6U9X2eUU'               ## Dev

def edit_customer(request, id: int) :
    """For when a Checklist Manager adds a customer"""

    template = loader.get_template('customers/customer_details_in_app.html')

    customer = get_customer_details(request, id)
    customer = save_customer_details(request, id, customer)

    days_until_expiry = get_days_until_expiry(customer.account_expiry_date)

    form = generate_customer_form(customer)

    context = {'customer': customer,
               'form': form,
               'days_until_expiry': days_until_expiry,
               'stripe_url': STRIPE_URL,
               'url_email': urllib.parse.quote(customer.email)}

    """If you have a new customer, after the initial page is saved,
        you want to be redirected to the customer's page."""
    if customer.id != None and id == 0:
        return redirect('edit_customer', customer.id)

    return HttpResponse(template.render(context, request))

def get_customer_details(request, id: int) -> Customer:
    if id == 0:
        customer = Customer()
        customer.account_expiry_date = datetime.date.today() + datetime.timedelta(days=15)
    else:
        customer = Customer.objects.get(id=id)

    return customer

def save_customer_details(request, id: int, customer: Customer) -> bool:
    if request.method == "POST":
        form = CustomerForm(request.POST)

        if form.is_valid():
            customer.firstname = form.cleaned_data['firstname']
            customer.lastname = form.cleaned_data['lastname']
            customer.customer_type = form.cleaned_data['customer_type']
            customer.customer_uuid = form.cleaned_data['customer_uuid']
            customer.email = form.cleaned_data['email']
            customer.company_name = form.cleaned_data['company_name']

            ## Add that if the email doesn't exist, add the customer.
            ## Then add the relationship
            ## Otherwise you just save the customer.

            if Customer.objects.filter(email=request.POST['email']).exists() and id == 0:
                messages.error(request, 'That email address already exists in our system.<br>Every account requires a unique email address.')
            elif customer._state.adding:
                customer.save()

                password = random_password_generator.random_password(15)
                manager = request.user                                  ## To get the manager related to this transaction.

                user = add_user(customer.firstname, customer.lastname, customer.email, password)
                add_customer_to_user_connection(user, customer, manager)
                send_welcome_email(customer, password)

                messages.success(request, 'User information was successfully updated.')
            else:
                customer.save()
                messages.success(request, 'User information was successfully updated.')

    return customer

def send_welcome_email(customer, password):

    context = {'customer': customer,
               'password': password}

    sendemail_with_template(customer.email, context)

    return True

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
    # customers = Customer.objects.all().order_by('id')

    related_customers = UsersToCustomerRelationship.objects.filter(manager=1).select_related('customer')
    customers = [item.customer for item in related_customers]

    context = { 'customers': customers }

    return HttpResponse(template.render(context, request))

def add_user(firstname: str, lastname: str, email: str, password: str) -> User:
    """Adds a new user when needed.
        Also updates the user/customer relationship."""

    # password = random_password_generator.random_password(12)

    user = User.objects.create_user(username=email, first_name=firstname, last_name=lastname, password=password)
    user.save()

    return user

def add_customer_to_user_connection(user: User, customer: Customer, manager: User) -> bool:
    relationship = UsersToCustomerRelationship()

    relationship.user = user
    relationship.customer = customer
    relationship.manager = manager
    relationship.is_active = True

    relationship.save()

    return True
