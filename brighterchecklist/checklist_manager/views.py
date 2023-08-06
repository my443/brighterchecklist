import datetime

from django.shortcuts import render, redirect
from django.http import HttpResponse
from django.template import loader
from .models import SourceChecklist, ChecklistTemplateItems
from .forms import ChecklistTemplateForm, ChecklistItemForm

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
        ## TODO - Change the owner here to be dynamic based on the the logged in user.
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
    checklist_info = SourceChecklist.objects.get(id=checklist_id)

    template = loader.get_template('checklist_template_main.html')

    context = {
        'all_template_items': all_template_items,
        'checklist_info': checklist_info
    }

    return HttpResponse(template.render(context))

def new_template_item(request, checklist_id):
    template = loader.get_template('checklist_template_entry.html')
    details = ChecklistTemplateItems()

    details.checklist_id = checklist_id
    #
    # data = {
    #     'item_short_text': details.item_short_text,
    #     'checklist_id': details.checklist_id,
    # }

    form = ChecklistItemForm()
    form.checklist_id = details.checklist_id

    context = {
        'details': details,
        'form': form
    }

    return HttpResponse(template.render(context, request))

def edit_template_item(request, item_id):
    details = ChecklistTemplateItems.objects.get(id=item_id)
    template = loader.get_template('checklist_template_entry.html')

    ## Put the values in the form
    data = {
        'item_short_text': details.template_item_short_text,
        'item_description': details.template_item_long_text,
        'checklist_id': details.checklist_id,
    }

    form = ChecklistItemForm(data)

    context = {
        'details': details,
        'form': form
    }
    return HttpResponse(template.render(context, request))

def save_template_item(request, item_id):
    # print (request.POST)
    # print (vars(request.POST))
    if item_id == 0:
        item_to_save = ChecklistTemplateItems()
        item_to_save.checklist_id = request.POST['checklist_id']
    else:
        item_to_save = ChecklistTemplateItems.objects.get(id=item_id)

    checklist_id = item_to_save.checklist_id

    form = ChecklistItemForm(request.POST)

    ## item_to_save.checklist_id = 25

    if form.is_valid():
        item_to_save.template_item_short_text = request.POST['item_short_text']
        item_to_save.template_item_long_text = form.cleaned_data['item_description']
        item_to_save.last_updated = datetime.datetime.now()

        item_to_save.save()

    return redirect(f'/manager/template/list/{checklist_id}')

def delete_template_item(request, item_id):
    pass