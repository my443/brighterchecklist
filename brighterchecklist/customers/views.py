import datetime

from django.shortcuts import render, redirect
from .models import Customer
from .forms import CustomerSignupForm
from .email import sendmail_simple, sendmail_by_class, sendemail_with_template
from django.template import loader
from django.http import HttpResponse
from django.contrib.auth.models import User

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

    send_email_after_save(customer)

    return thankyou(request)

def send_email_after_save(customer):
    context = { 'customer': customer }
    sendemail_with_template(customer.email, context)

    return 0

def thankyou(request):
    template = loader.get_template('customers/thankyou.html')
    context = {}

    return HttpResponse(template.render(context, request))

def profile(request):
    template = loader.get_template('customers/customer_profile.html')
    user = request.user

    user_to_update = User.objects.get(pk=request.user.pk)
    
    if request.method == "POST":
        form = CustomerSignupForm(request.POST)

        if form.is_valid():
            user_to_update.first_name = form.firstname
            user_to_update.last_name = form.lastname

            user_to_update.save()

            return redirect('profile')
    else:
        inital = {'first_name': user.first_name, 'last_name':user.last_name}
        form = CustomerSignupForm(initial=inital)

    form.fields['firstname'].widget.attrs['class']='w-75'  ## Assign a class to the form field
    form.fields['lastname'].widget.attrs['class'] = 'w-75'

    context = {'form': form}

    return HttpResponse(template.render(context, request))

def something_to_test():
    return 'hello world'


