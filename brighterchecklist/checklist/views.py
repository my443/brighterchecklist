from django.shortcuts import render
from django.http import HttpResponse, HttpResponseRedirect
from django.template import loader
from .models import Checklist
from .forms import ChecklistForm
from pprint import pprint


# Create your views here.
def checklist(request):
    checklist_items = Checklist.objects.all()

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

    checklist_items = Checklist.objects.all()

    template = loader.get_template('checklist/checklist_items_list.html')

    context = {
        'checklist_items': checklist_items
    }

    return HttpResponse(template.render(context, request))