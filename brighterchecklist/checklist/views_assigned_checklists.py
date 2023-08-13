from django.shortcuts import render
from django.http import HttpResponse, HttpResponseRedirect
from django.template import loader
from django.db.models import Q, Count
from .models import Checklist, ChecklistHeader
from .forms import ChecklistForm, AssignedChecklistForm
from pprint import pprint
import enumerations

def list_assigned_checklists(request):
    # assigned_checklists = ChecklistHeader.objects.all()
    assigned_checklists = ChecklistHeader.objects.annotate(number_of_incomplete=Count('checklist', filter=Q(checklist__iscomplete=False)))
    template = loader.get_template('checklist/assigned_checklists_list.html')

    context = {
        'assigned_checklists': assigned_checklists,
        'navigation': enumerations.Navigation.checklist.name,
    }

    return HttpResponse(template.render(context, request))

def edit_assigned_checklist_notes(request, id):
    details = ChecklistHeader.objects.get(id=id)
    template = loader.get_template('checklist/assigned_checklist_notes_entry.html')
    navigation = 'checklist'

    data = {
        'assigned_checklist_notes': details.checklist_notes,
    }

    form = AssignedChecklistForm(data)

    context = {
        'details': details,
        'form': form,
        'navigation': enumerations.Navigation.checklist.name,
    }
    return HttpResponse(template.render(context, request))

def save_assigned_checklist_notes(request, id):
    details = ChecklistHeader.objects.get(id=id)

    if request.method == 'POST':
        form = AssignedChecklistForm(request.POST)

    if form.is_valid():
        details.checklist_notes =  form.cleaned_data['assigned_checklist_notes']

        # Only resave the details if the form is valid.
        details.save()

    return HttpResponseRedirect(f"/checklist/assigned/")
