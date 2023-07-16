from django.shortcuts import render
from django.http import HttpResponse, HttpResponseRedirect
from django.template import loader
from .models import Checklist
from .forms import ChecklistForm
from pprint import pprint


# Create your views here.
def checklist(request):
    checklist_items = Checklist.objects.all()

    template = loader.get_template('checklist.html')

    context = {
        'checklist_items': checklist_items
    }
    # x = request.__dict__
    # pprint(vars(request))
    return HttpResponse(template.render(context, request))
    # return HttpResponse('<h1>This is your checklist.</h1>')

def details(request, id):
    details = Checklist.objects.get(id=id)
    template = loader.get_template('details.html')

    if request.method == 'POST':
        form = ChecklistForm(request.POST)

        if form.is_valid():
            new_checklist = Checklist()
            new_checklist.source = form.cleaned_data['source']
            new_checklist.startdate = form.cleaned_data['startdate']
            new_checklist.iscomplete = form.cleaned_data['iscomplete']

            new_checklist.save()
            # process the data in form.cleaned_data as required
            # ...
            # redirect to a new URL:
            return HttpResponseRedirect("/checklist/")
    else:
        form = ChecklistForm()

    context = {
        'details': details,
        'form': form
    }
    return HttpResponse(template.render(context, request))
