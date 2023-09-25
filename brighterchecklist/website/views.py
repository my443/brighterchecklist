from django.shortcuts import render
from django.template import loader
from django.http import HttpResponse, HttpResponseRedirect
from .models import Feedback

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

def submit_feedback(request):
    feedback = Feedback()
    print (request)
    feedback.user_giving_feedback = request.user

    feedback.feedback_text = request.POST.get('feedback_text', False)
    feedback.save()

    print (request.path_info)
    return HttpResponseRedirect(request.META.get('HTTP_REFERER'))

