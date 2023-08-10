from django.shortcuts import render, redirect
from django.http import HttpResponse
from django.template import loader
from .models import SourceChecklist, ChecklistTemplateItems
from .forms import ChecklistTemplateForm, ChecklistItemForm
import datetime, enumerations

def list_template_items(request, checklist_id):
    ## TODO - Check to make sure that the user is allowed access to this checklist. (Before you show the checklist details.)
    all_template_items = ChecklistTemplateItems.objects.all().filter(checklist_id=checklist_id)
    checklist_info = SourceChecklist.objects.get(id=checklist_id)

    template = loader.get_template('manager/checklist_template_main.html')

    context = {
        'all_template_items': all_template_items,
        'checklist_info': checklist_info,
        'navigation': enumerations.Navigation.manager.name,
    }

    return HttpResponse(template.render(context))

def new_template_item(request, checklist_id):
    template = loader.get_template('manager/checklist_template_entry.html')
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
        'form': form,
        'navigation': enumerations.Navigation.manager.name,
    }

    return HttpResponse(template.render(context, request))

def edit_template_item(request, item_id):
    details = ChecklistTemplateItems.objects.get(id=item_id)
    template = loader.get_template('manager/checklist_template_entry.html')

    ## Put the values in the form
    data = {
        'item_short_text': details.template_item_short_text,
        'item_description': details.template_item_long_text,
        'checklist_id': details.checklist_id,
    }

    form = ChecklistItemForm(data)

    context = {
        'details': details,
        'form': form,
        'navigation': enumerations.Navigation.manager.name,
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
    checklist_item_to_delete = ChecklistTemplateItems.objects.get(id=item_id)
    checklist_id = checklist_item_to_delete.checklist_id
    checklist_item_to_delete.delete()

    return redirect(f'/manager/template/list/{checklist_id}')