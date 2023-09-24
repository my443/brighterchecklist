from django.shortcuts import render
from django.template import loader
from django.http import HttpResponse

# Create your views here.


def home(request):
    template = loader.get_template('website/index.html')

    context = {}

    # return render(request, template)
    return HttpResponse(template.render(context, request))

def privacy_policy(request):
    template = loader.get_template('website/privacy_policy.html')

    context = {}

    # return render(request, template)
    return HttpResponse(template.render(context, request))

def terms_of_use(request):
    template = loader.get_template('website/terms_of_use.html')

    context = {}

    # return render(request, template)
    return HttpResponse(template.render(context, request))