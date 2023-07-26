from django.shortcuts import render
from django.http import HttpResponse
from django.template import loader
from .models import SourceChecklist
from .forms import ChecklistTemplateForm

def manager(request):
    if request.method == 'POST':
        form = ChecklistTemplateForm(request.POST)
        print (request.POST)

        source = SourceChecklist()
        source.owner = 1

        if form.is_valid():
            source.checklist_name = request.POST['checklist_name']
            source.checklist_details = form.cleaned_data['checklist_details']

        source.save()

    template = loader.get_template('checklist_manager_main.html')
    return HttpResponse(template.render())

def new(request):
    new_checklist = SourceChecklist()
    form = ChecklistTemplateForm()
    template = loader.get_template('checklist_manager_entry.html')
    context = {
        'form': form,
    }
    return HttpResponse(template.render(context, request))