from django.shortcuts import render
from .models import Customer
from django.template import loader
from django.http import HttpResponse
from django.shortcuts import redirect

def new_customer_signup(request):
    # template = loader.get_template('website/index.html')

    new_customer = Customer()
    new_customer.email = request.POST['emailAddress']

    new_customer.save()

    # context = {}

    return show_customer_signup_details_form(request)
    # return HttpResponse(template.render(context, request))



def show_customer_signup_details_form(request):
    return redirect('/')

def save_customer_sign_up_details(request):
    pass


