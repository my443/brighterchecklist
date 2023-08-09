from django.shortcuts import render
from django.http import HttpResponse, HttpResponseRedirect
from django.template import loader
from .models import Checklist, ChecklistHeader
from .forms import ChecklistForm
from pprint import pprint

# Create your views here.
def checklist(request,id):
    checklist_items = Checklist.objects.all().filter(checklist_header_id=id)

    template = loader.get_template('checklist/checklist_items_list.html')

    context = {
        'checklist_items': checklist_items
    }
    # x = request.__dict__
    # pprint(vars(request))
    return HttpResponse(template.render(context, request))
    # return HttpResponse('<h1>This is your checklist.</h1>')

def edit_notes(request, id):
    details = Checklist.objects.get(id=id)
    template = loader.get_template('checklist/checklist_item_notes_entry.html')

    data = {
        'checklist_item_users_notes': details.checklist_item_users_notes,
    }

    form = ChecklistForm(data)

    context = {
        'details': details,
        'form': form
    }
    return HttpResponse(template.render(context, request))

def save_notes(request, id):
    details = Checklist.objects.get(id=id)

    if request.method == 'POST':
        form = ChecklistForm(request.POST)

    if form.is_valid():
        details.checklist_item_users_notes =  form.cleaned_data['checklist_item_users_notes']

        # Only resave the details if the form is valid.
        details.save()

    return HttpResponseRedirect("/checklist/")


def complete_item(request, id):
    checklist_item = Checklist.objects.get(id=id)

    if checklist_item.iscomplete:
        checklist_item.iscomplete = False
    else:
        checklist_item.iscomplete = True

    checklist_item.save()

    return HttpResponseRedirect(f"/checklist/{checklist_item.checklist_header.id}")

def list_assigned_checklists(request):
    assigned_checklists = ChecklistHeader.objects.all()
    template = loader.get_template('checklist/assigned_checklists_list.html')

    context = {
        'assigned_checklists': assigned_checklists,
    }

    return HttpResponse(template.render(context, request))