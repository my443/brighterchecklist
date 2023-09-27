import datetime

from django.contrib.auth.models import User
from .models import Customer, UsersToCustomerRelationship
import shared.random_password_generator as random_password_generator
from django.shortcuts import redirect
from django.contrib import messages
from .views_customer import add_user, add_customer_to_user_connection, send_welcome_email
from checklist_manager.models import SourceChecklist, ChecklistTemplateItems
from checklist_manager.views_assign_checklist_to_user import assign_checklist_to_person


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

    add_starter_checklist_for_customer(user)

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

def add_starter_checklist_for_customer(user):
    """When a customer first signs up, a starter checklist is added for them."""
    checklist = SourceChecklist()

    checklist.checklist_name = "Checklist for setting up checklists"
    checklist.checklist_details  = """<h3>Use this checklist every time you are creating a new checklist.</h3>
                                        <p>First you will create all of the checklist items that you will do over and over. 
                                        This is the template for the repeatable checklist. Then you will assign the checklist
                                        to yourself or others. When the checklist is assigned, you can start to check of the items
                                        that are done.</p>"""
    checklist.owner = user

    checklist.save()

    list_of_template_items = [
        ["""Click on Checklist Template in the left-side navigation bar.""",""""""]
        , ["""Click the 'Add Checklist' button""","""Add your checklist name and description if you want."""]
        , ["""Click on the checklist you just created.""", """"""]
        , ["""Click the 'Add New Checklist Item' button""", """Add the details of the task that needs to be done. Repeat this step until you have all of your tasks in the checklist."""]
        , ["""Click 'Assign To User'""", """If you have many checklist completers who report to you, you will see a list of people who you can assign the list to. Otherwise, you will be taken directly to the checklist to complete."""]
        , ["""Check off items on the checklist.""", """Happy completing!"""]
    ]

    for item in list_of_template_items:
        checklist_item = ChecklistTemplateItems()
        checklist_item.template_item_short_text = item[0]
        checklist_item.template_item_long_text = item[1]
        checklist_item.source_checklist = checklist
        checklist_item.save()

    ## Creates an empty object
    ## https://stackoverflow.com/questions/19476816/creating-an-empty-object-in-python
    request = type('', (), {})()
    request.user = user

    assign_checklist_to_person(request=request, checklist_id=checklist.id, user_id=user.id)

    return True
