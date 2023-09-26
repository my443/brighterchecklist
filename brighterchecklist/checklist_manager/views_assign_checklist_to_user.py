from django.contrib.auth.models import User
from django.shortcuts import render, redirect
from django.http import HttpResponse
from django.template import loader
from .models import SourceChecklist, ChecklistTemplateItems
from customers.models import UsersToCustomerRelationship
from checklist.models import Checklist, ChecklistHeader
import enumerations
from shared.security_check import check_security

import datetime

def all_users_for_assignment(request, checklist_id, all_users):
    ## SECURITY: We can filter by **all** of the users a person is allowed to see.
    ## TODO: This needs to be updated when there are checklist completers. Needs to include the relationship of users for that manager.
    # all_users = User.objects.all().filter(id=request.user.id)
    checklist_info = SourceChecklist.objects.get(id=checklist_id)

    # template = loader.get_template('manager/assign_checklist_to_person.html')

    ## TODO - Add the analytics for the specific checklist that has been assigned.
    ##          Based on checklist_id

    context = {
        'all_users': all_users,
        'checklist_info': checklist_info,
        'navigation': enumerations.Navigation.manager.name,
        # 'checklist_analytics': checklist_analytics,
    }

    return context
    # return HttpResponse(template.render(context))

def assign_checklist_from_list(request, checklist_id, user_id):
    assign_checklist_to_person(request, checklist_id, user_id)

    return redirect(f'/manager/users/{checklist_id}')

def assign_checklist_to_person(request, checklist_id, user_id):
    checklist_info = SourceChecklist.objects.get(id=checklist_id)
    # checklist_template_items = ChecklistTemplateItems.objects.all().filter(checklist_id=checklist_id)
    checklist_template_items = ChecklistTemplateItems.objects.all().filter(source_checklist=checklist_info)

    if check_security(checklist_info.owner, request.user):
        ## Set the checklist header
        checklist_header = ChecklistHeader()
        checklist_header.source_checklist = checklist_info
        checklist_header.checklist_notes = checklist_info.checklist_details
        checklist_header.assigned_to_user_id = user_id
        checklist_header.checklist_startdate = datetime.datetime.now()
        checklist_header.checklist_custom_title = '<Assigned '+datetime.datetime.now().strftime("%Y-%m-%d")+'> ' + checklist_info.checklist_name
        checklist_header.save()

        ## Set the checklist items
        for item in checklist_template_items:
            checklist_item = Checklist()
            checklist_item.checklist_header = checklist_header
            checklist_item.checklist_item_short_text = item.template_item_short_text
            # checklist_item.checklist_item_long_text_text = item.template_item_long_text
            checklist_item.checklist_item_users_notes = item.template_item_long_text

            # print (item.template_item_long_text)

            checklist_item.save()

    return checklist_header.id

    # return redirect(f'/manager/users/{checklist_id}')

def assign_checklist_or_list_completers(request, checklist_id):
    """If a manager only has one completer, automatcially assign the checklist.
    Otherwise, show the list of checklists to be asigned."""

    template = loader.get_template('manager/assign_checklist_to_person.html')

    all_users = UsersToCustomerRelationship.objects.all().filter(manager=request.user)

    if all_users.count() > 1:
        context = all_users_for_assignment(request, checklist_id, all_users)
        return HttpResponse(template.render(context))
        # return redirect(f'/manager/users/{checklist_id}')
    else:
        assigned_checklist_id = assign_checklist_to_person(request, checklist_id, request.user.id)
        return redirect(f'/checklist/{assigned_checklist_id}')
