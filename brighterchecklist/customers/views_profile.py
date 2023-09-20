from django.contrib.auth.models import User
from django.http import HttpResponse
from django.shortcuts import redirect
from django.template import loader
from .forms import ProfileUpdateForm
from .models import UsersToCustomerRelationship
from .views_customer_helpers import get_days_until_expiry


def profile(request):
    ##TODO - [Future Refactor] The user profile should be aligned with the customer profile. (So that they are updating the same thing.)
    ##TODO - [Future Refactor] When someone updates their Customer name, it should update their user profile also.
    template = loader.get_template('customers/customer_self_profile.html')
    user = request.user

    user_to_update = User.objects.get(pk=request.user.pk)
    customer = UsersToCustomerRelationship.objects.get(user_id=request.user.pk).customer
    print (customer.id)

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

    days_until_expiry = get_days_until_expiry(customer.account_expiry_date)

    context = {'form': form,
               'days_until_expiry': days_until_expiry,
               'customer': customer }

    return HttpResponse(template.render(context, request))
