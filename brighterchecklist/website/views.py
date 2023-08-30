from django.shortcuts import render
from django.template import loader
from django.http import HttpResponse

# Create your views here.


def home(request):
    template = loader.get_template('website/index.html')

    context = {}

    # return render(request, template)
    return HttpResponse(template.render(context, request))

def sign_up_user(request):
    pass