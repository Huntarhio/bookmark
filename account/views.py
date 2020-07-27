from django.shortcuts import render
from django.contrib.auth.decorators import login_required
from .forms import LoginForm, UserRegistrationForm, UserEditForm, ProfileEditForm
from .models import Profile
from django.contrib import messages


# Create your views here.

from django.http import HttpResponse
from django.contrib.auth import authenticate, login
from .forms import LoginForm

def user_login(request):
    if request.method == 'POST': #if the request made is a post request
        form = LoginForm(request.POST)
        if form.is_valid(): #checks if all form entries are valid
            cd = form.cleaned_data #cleans the valid form data
            user = authenticate(username=cd['username'], password=cd['password']) #authenticate the user with the submitted username and pasword
            if user is not None: #checks if the user is in the database
                if user.is_active:  # if the user is in database, checks if the user is an active users
                    login(request, user) #log the user in and return an http response
                    return HttpResponse('Authenticated '\
                    'successfully')
                else:
                    return HttpResponse('Disabled account') #if the user is in database but is an inactive user, return a response
            else:
                return HttpResponse('Invalid login') #if the user login is not in database, return invalid log in
    else:
        form = LoginForm() #if the request made is a get request
    return render(request, 'account/login.html', {'form': form})

@login_required   # sets the view with a compulsory login authentication
def dashboard(request):
    return render(request,'account/dashboard.html',
                            {'section': 'dashboard'}) # this shows the dashboard


def register(request):
    if request.method == 'POST':
        user_form = UserRegistrationForm(request.POST)
        if user_form.is_valid():
        # Create a new user object but avoid saving it yet
            new_user = user_form.save(commit=False)
            
            # Set the chosen password
            new_user.set_password(user_form.cleaned_data['password'])
            # Save the User object
            new_user.save()
            # Create the user profile
            profile = Profile.objects.create(user=new_user)
            return render(request,'account/register_done.html',{'new_user': new_user})
    else:
        user_form = UserRegistrationForm()
    return render(request,'account/register.html',{'user_form': user_form})

@login_required
def edit(request):
    if request.method == 'POST':
        user_form = UserEditForm(instance=request.user, data=request.POST)
        profile_form = ProfileEditForm(instance=request.user.profile, data=request.POST, files=request.FILES)

        if user_form.is_valid() and profile_form.is_valid():
            user_form.save()
            profile_form.save()
            messages.success(request, 'Profile updated successfully')
        else:
            messages.error(request, 'Error updating profile')
    else:
        user_form = UserEditForm(instance=request.user)
        profile_form = ProfileEditForm(instance=request.user.profile)
        # profile_form = ProfileForm(instance=request.user.userprofile)

    
    return render(request, 'account/edit.html', 
                        {'user_form':user_form,
                        'profile_form':profile_form})      
