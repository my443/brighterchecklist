from django.shortcuts import render
from django.http import HttpResponse
from django.template import loader

def manager(request):
    template = loader.get_template('checklist_manager_main.html')
    return HttpResponse(template.render())