from django.shortcuts import render, redirect
from django.http import HttpResponse
from django.template import loader
from .models import SourceChecklist, ChecklistTemplateItems
from .forms import ChecklistTemplateForm

def manager(request):
    all_checklists = SourceChecklist.objects.all()
    template = loader.get_template('checklist_manager_main.html')

    if request.method == 'POST':
        form = ChecklistTemplateForm(request.POST)
        print (request.POST)

        source = SourceChecklist()
        source.owner = 1

        if form.is_valid():
            source.checklist_name = request.POST['checklist_name']
            source.checklist_details = form.cleaned_data['checklist_details']

        source.save()

        return redirect('/manager/')

    context = {
        'all_checklists': all_checklists,
    }

    return HttpResponse(template.render(context))

def new(request):
    new_checklist = SourceChecklist()
    form = ChecklistTemplateForm()
    template = loader.get_template('checklist_manager_entry.html')
    context = {
        'form': form,
    }

    return HttpResponse(template.render(context, request))

def delete(request, id):
    checklist_to_delete = SourceChecklist.objects.get(id=id)
    checklist_to_delete.delete()

    return redirect('/manager/')

def edit(request, id):
    checklist_data = SourceChecklist.objects.get(id=id)
    template = loader.get_template('checklist_manager_entry.html')

    ## Put the values in the form
    data = {
        'checklist_name':checklist_data.checklist_name,
        'checklist_details':checklist_data.checklist_details
    }
    form = ChecklistTemplateForm(data)
    # print (vars(form))

    context = {
        'form': form,
        'checklist_data': checklist_data,
    }

    return HttpResponse(template.render(context, request))

def save(request, id):
    if id == 0:
        checklist_to_update = SourceChecklist(owner=1)
    else:
        checklist_to_update = SourceChecklist.objects.get(id=id)

    form = ChecklistTemplateForm(request.POST)

    if form.is_valid():
        checklist_to_update.checklist_name = request.POST['checklist_name']
        checklist_to_update.checklist_details = form.cleaned_data['checklist_details']

        checklist_to_update.save()

    return redirect('/manager/')

def list_template_items(request, checklist_id):
    ## TODO - Check to make sure that the user is allowed access to this checklist. (Before you show the checklist details.)
    all_template_items = ChecklistTemplateItems.objects.all().filter(checklist_id=checklist_id)

    template = loader.get_template('checklist_template_main.html')

    context = {
        'all_template_items': all_template_items,
    }

    return HttpResponse(template.render(context))

def add_template_item(request, checklist_id):
    pass

def edit_tempalte_item(request, item_id):
    pass

def delete_template_item(request, item_id):
    pass