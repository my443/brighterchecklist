from django.contrib.auth.models import User
from django.shortcuts import render, redirect
from django.http import HttpResponse
from django.template import loader
from .models import SourceChecklist, ChecklistTemplateItems
from checklist.models import Checklist, ChecklistHeader
# from models import users

import datetime

def all_users_for_assignment(request, checklist_id):
    all_users = User.objects.all()
    checklist_info = SourceChecklist.objects.get(id=checklist_id)

    template = loader.get_template('manager/assign_checklist_to_person.html')

    ## TODO - Add the analytics for the specific checklist that has been assigned.
    ##          Based on checklist_id

    context = {
        'all_users': all_users,
        'checklist_info': checklist_info,
        # 'checklist_analytics': checklist_analytics,
    }

    return HttpResponse(template.render(context))

def assign_checklist_to_person(request, checklist_id, user_id):
    checklist_info = SourceChecklist.objects.get(id=checklist_id)
    checklist_template_items = ChecklistTemplateItems.objects.all().filter(checklist_id=checklist_id)

    ## Set the checklist header
    checklist_header = ChecklistHeader()
    checklist_header.source_checklist_id = checklist_info
    checklist_header.assigned_to_user_id = user_id
    checklist_header.checklist_startdate = datetime.datetime.now()
    checklist_header.checklist_custom_title = '<Assigned '+datetime.datetime.now().strftime("%Y-%m-%d")+'> ' + checklist_info.checklist_name
    checklist_header.save()

    ## Set the checklist items
    for item in checklist_template_items:
        checklist_item = Checklist()
        checklist_item.checklist_header = checklist_header
        checklist_item.checklist_item_short_text = item.template_item_short_text
        checklist_item.checklist_item_long_text_text = item.template_item_long_text

        checklist_item.save()

    return redirect(f'/manager/users/{checklist_id}')

