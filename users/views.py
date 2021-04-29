from django.shortcuts import render, redirect
from django.contrib import messages 
from .forms import UserRegisterForm, UserProfileForm, UserStoreForm
from django.contrib.auth.decorators import login_required
from django.contrib.auth.models import User
from .models import Profile, UserProfile
from dashboard.models import stores

def register(request): 
    if request.method == 'POST':
        form = UserRegisterForm(request.POST)
        profileform = UserProfileForm(request.POST)
        storeform = UserStoreForm(request.POST)
        if form.is_valid(): 
            form.save()
            profileform.save()
            storeform.save()
            username = form.cleaned_data.get('username')
            messages.success(request, f'Account created, welcome {username}!')
            return redirect('login')
    else :
        form = UserRegisterForm()
        profileform = UserProfileForm()
        storeform = UserStoreForm()
    return render(request, 'users/register.html', {'form': form ,'profileform': profileform,'storeform': storeform })

@login_required
def profile(request): 
    return render(request, 'users/profile.html')

