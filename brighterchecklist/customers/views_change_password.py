from django.shortcuts import render
from django.contrib.auth.forms import PasswordChangeForm
from django.contrib.auth import update_session_auth_hash
from django.shortcuts import redirect
from django.contrib.auth.decorators import login_required

# https://www.programcreek.com/python/example/50650/django.contrib.auth.forms.PasswordChangeForm

## TODO - Add @login_required decorator
## TODO - Put this link somewhere useful.
## TODO - Move the template to the registration template folder.

@login_required
def change_password(request):
    """View function for the user profile, profile.html."""
    # Get the current user's user object
    # user = request.user
    # # Look-up the username in the database
    # current_user_name = User.objects.get(username=user.username)
    # current_user_avatar = UserProfile.objects.get(user=user.id)
    # If ths is a POST, process it as a password update
    if request.method == 'POST':
        form = PasswordChangeForm(request.user, request.POST)
        if form.is_valid():
            user = form.save()
            # This is a VERY important step!
            update_session_auth_hash(request, user)
            # messages.success(request,
            #                  'Your password was successfully updated!',
            #                  extra_tags='alert-success')
            return redirect('/manager')
    else:
        form = PasswordChangeForm(request.user)

    return render(request, 'registration/password_change.html', {
        'form': form,
        'user': request.user,
        # 'current_user': current_user_name,
        # 'user_avatar': current_user_avatar
    })