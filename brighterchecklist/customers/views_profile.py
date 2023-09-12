from django.contrib.auth.models import User
from django.http import HttpResponse
from django.shortcuts import redirect
from django.template import loader
from .forms import ProfileUpdateForm


def profile(request):
    template = loader.get_template('customers/customer_profile.html')
    user = request.user

    user_to_update = User.objects.get(pk=request.user.pk)

    if request.method == "POST":
        form = ProfileUpdateForm(request.POST)

        if form.is_valid():
            user_to_update.first_name = form.cleaned_data['first_name']
            user_to_update.last_name = form.cleaned_data['last_name']

            user_to_update.save()

            return redirect('profile')
    else:
        inital = {'first_name': user.first_name, 'last_name':user.last_name}
        form = ProfileUpdateForm(initial=inital)

    # form.fields['first_name'].widget.attrs['class']='w-75'  ## Assign a class to the form field
    # form.fields['last_name'].widget.attrs['class'] = 'w-75'

    context = {'form': form}

    return HttpResponse(template.render(context, request))
