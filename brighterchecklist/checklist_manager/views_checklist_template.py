from django.shortcuts import render, redirect
from django.http import HttpResponse
from django.template import loader
from .models import SourceChecklist, ChecklistTemplateItems
from .forms import ChecklistTemplateForm, ChecklistItemForm
import datetime, enumerations
from shared.security_check import check_security

def list_template_items(request, checklist_id):
    ## TODO - Check to make sure that the user is allowed access to this checklist. (Before you show the checklist details.)
    all_template_items = ChecklistTemplateItems.objects.all().filter(source_checklist=checklist_id)         # Use the model's FK to reference checklist ID. (It is safer)
    checklist_info = SourceChecklist.objects.get(id=checklist_id)

    if not check_security(checklist_info.owner, request.user):
        return redirect('/manager/')

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
    source_checklist = SourceChecklist.objects.get(id=checklist_id)

    if not check_security(source_checklist.owner, request.user):
        return redirect('/manager/')

    details.source_checklist = source_checklist
    #
    # data = {
    #     'item_short_text': details.item_short_text,
    #     'checklist_id': details.checklist_id,
    # }

    form = ChecklistItemForm()
    form.checklist_id = details.source_checklist

    context = {
        'details': details,
        'form': form,
        'navigation': enumerations.Navigation.manager.name,
    }

    return HttpResponse(template.render(context, request))

def edit_template_item(request, item_id):
    details = ChecklistTemplateItems.objects.get(id=item_id)

    if not check_security(details.source_checklist.owner, request.user):
        return redirect('/manager/')

    template = loader.get_template('manager/checklist_template_entry.html')

    ## Put the values in the form
    data = {
        'item_short_text': details.template_item_short_text,
        'item_description': details.template_item_long_text,
        'checklist_id': details.source_checklist.id,
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
        checklist_id  = request.POST['checklist_id']

        source_checklist = SourceChecklist.objects.get(id=checklist_id)
        item_to_save.source_checklist = source_checklist
        # item_to_save.checklist_id = request.POST['checklist_id']
    else:
        item_to_save = ChecklistTemplateItems.objects.get(id=item_id)

    checklist = item_to_save.source_checklist

    if not check_security(checklist.owner, request.user):
        return redirect('/manager/')

    form = ChecklistItemForm(request.POST)

    ## item_to_save.checklist_id = 25

    if form.is_valid():
        item_to_save.template_item_short_text = request.POST['item_short_text']
        item_to_save.template_item_long_text = form.cleaned_data['item_description']
        item_to_save.last_updated = datetime.datetime.now()

        item_to_save.save()

    return redirect(f'/manager/template/list/{checklist.id}')

def delete_template_item(request, item_id):
    checklist_item_to_delete = ChecklistTemplateItems.objects.get(id=item_id)
    source_checklist = checklist_item_to_delete.source_checklist

    if not check_security(source_checklist.owner, request.user):
        return redirect('/manager/')

    checklist_item_to_delete.delete()

    return redirect(f'/manager/template/list/{source_checklist.id}')

def test_editor(request):
    template = loader.get_template('manager/editor_testing.html')
    context = {}
    return HttpResponse(template.render(context, request))