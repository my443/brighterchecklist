from django.shortcuts import render, redirect
from django.http import HttpResponse
from django.template import loader
from .models import SourceChecklist
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
    form = ChecklistTemplateForm()
    template = loader.get_template('checklist_manager_entry.html')

    ## Put the values in the form
    form.checklist_name = checklist_data.checklist_name
    form.checklist_details = checklist_data.checklist_details

    data = {
        'checklist_name':checklist_data.checklist_name,
        'checklist_details':checklist_data.checklist_details
    }
    form = ChecklistTemplateForm(data)
    print (form)

    context = {
        'form': form,
    }

    return HttpResponse(template.render(context, request))