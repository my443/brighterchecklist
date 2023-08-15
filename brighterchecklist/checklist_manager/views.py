from django.shortcuts import render, redirect
from django.http import HttpResponse
from django.template import loader
from .models import SourceChecklist, ChecklistTemplateItems
from .forms import ChecklistTemplateForm, ChecklistItemForm
from .views_checklist_template import *
from .views_assign_checklist_to_user import *
import datetime, enumerations
from django.contrib.auth.decorators import login_required
from django.contrib.auth.models import User, Permission

@login_required
def manager(request):
    all_checklists = SourceChecklist.objects.all()
    template = loader.get_template('manager/checklist_manager_main.html')

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
        'navigation': enumerations.Navigation.manager.name,
    }


    # https://stackoverflow.com/questions/30559020/django-login-template-doesnt-recognize-logged-user
    # return render(request, 'manager/checklist_manager_main.html', context)
    return HttpResponse(template.render(context, request))

@login_required
def new(request):
    new_checklist = SourceChecklist()
    form = ChecklistTemplateForm()
    template = loader.get_template('manager/checklist_manager_entry.html')
    context = {
        'form': form,
        'navigation': enumerations.Navigation.manager.name,
    }

    return HttpResponse(template.render(context, request))

@login_required
def delete(request, id):
    checklist_to_delete = SourceChecklist.objects.get(id=id)
    checklist_to_delete.delete()

    return redirect('/manager/')

@login_required
def edit(request, id):
    checklist_data = SourceChecklist.objects.get(id=id)
    template = loader.get_template('manager/checklist_manager_entry.html')

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
        'navigation': enumerations.Navigation.manager.name,
    }

    return HttpResponse(template.render(context, request))

@login_required
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



