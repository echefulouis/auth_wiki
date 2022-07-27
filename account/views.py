from operator import is_
from django.shortcuts import render, redirect
from django.contrib.auth import login, authenticate, logout
from django.contrib.auth.forms import UserCreationForm
from django.contrib import messages
from django.contrib.auth.decorators import login_required
from .forms import UpdateUserForm, UpdateProfileForm
from django.urls import reverse_lazy
from django.contrib.auth.views import PasswordChangeView
from django.contrib.messages.views import SuccessMessageMixin

from account.forms import SignupForm

# Create your views here.

def home(request):
    return render(request, "home.html")
    

def signup(request):
    form =SignupForm(request.POST)
    if request.method == 'POST':
        form =SignupForm(request.POST)
        
        if form.is_valid():
            form.save()
            username =form.cleaned_data.get('username')
            raw_password =form.cleaned_data.get('password1')
            user =authenticate(username=username, password=raw_password)
            login(request,user)
            return redirect('home')
    
        else:
            messages.info(request, 'Cannot sign up. Please, refill the form correctly') 
    context = {'form': form}
    return render(request, 'signup.html', context)



def loginpage(request):
    if request.method == 'POST':
        username = request.POST.get('username')
        raw_password = request.POST.get('password')

        user = authenticate(request, username=username, password=raw_password)
        if user is not None:
            login(request, user)
            return redirect('home')
        else:
                messages.error(request,'Username Or Password Is Incorrect')

    context = {} 
    return render(request, 'login.html', context)  


def userlogout(request):
    logout(request)
    return redirect('home')


@login_required
def profile(request):
    if request.method == 'POST':
        user_form = UpdateUserForm(request.POST, instance=request.user)
        profile_form = UpdateProfileForm(request.POST, request.FILES, instance=request.user.profile)

        if user_form.is_valid() and profile_form.is_valid():
            user_form.save()
            profile_form.save()
            messages.success(request, 'Your profile is updated successfully')
            return redirect(to='account-profile')

        else:
            user_form = UpdateUserForm(instance=request.user)
            profile_form = UpdateProfileForm(instance=request.user.profile)


        return render(request, 'profile.html', {'user_form': user_form, 'profile_form': profile_form})

    return render(request, 'profile.html', {'user_form': 'user_form', 'profile_form': 'profile_form'})


class ChangePasswordView(SuccessMessageMixin, PasswordChangeView):
    template_name = 'account/change_password.html'
    success_message = "Successfully Changed Your Password"
    success_url = reverse_lazy('account-home')

    #context = {'entry': entry, 'topic': topic, 'form': form}
    #return render(request, 'edit_entry.html', context)