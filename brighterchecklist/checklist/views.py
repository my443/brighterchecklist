from django.shortcuts import render
from django.http import HttpResponse, HttpResponseRedirect
from django.template import loader
from django.db.models import Q, Count
from .models import Checklist, ChecklistHeader
from .forms import ChecklistForm, AssignedChecklistForm
from .views_assigned_checklists import *
from pprint import pprint
import enumerations

# Create your views here.
def checklist(request,id):
    checklist_items = Checklist.objects.all().filter(checklist_header_id=id)

    template = loader.get_template('checklist/checklist_items_list.html')

    context = {
        'checklist_items': checklist_items,
        'navigation': enumerations.Navigation.checklist.name,
    }
    # x = request.__dict__
    # pprint(vars(request))
    return HttpResponse(template.render(context, request))
    # return HttpResponse('<h1>This is your checklist.</h1>')

def edit_notes(request, id):
    details = Checklist.objects.get(id=id)
    template = loader.get_template('checklist/checklist_item_notes_entry.html')
    navigation = 'checklist'

    data = {
        'checklist_item_users_notes': details.checklist_item_users_notes,
    }

    form = ChecklistForm(data)

    context = {
        'details': details,
        'form': form,
        'navigation': enumerations.Navigation.checklist.name,
    }
    return HttpResponse(template.render(context, request))

def save_checklist_item_notes(request, id):
    details = Checklist.objects.get(id=id)
    checklist = details.checklist_header

    if request.method == 'POST':
        form = ChecklistForm(request.POST)

    if form.is_valid():
        details.checklist_item_users_notes =  form.cleaned_data['checklist_item_users_notes']

        # Only resave the details if the form is valid.
        details.save()

    return HttpResponseRedirect(f"/checklist/{checklist.id}")

def complete_item(request, id):
    checklist_item = Checklist.objects.get(id=id)

    if checklist_item.iscomplete:
        checklist_item.iscomplete = False
    else:
        checklist_item.iscomplete = True

    checklist_item.save()

    return HttpResponseRedirect(f"/checklist/{checklist_item.checklist_header.id}")

