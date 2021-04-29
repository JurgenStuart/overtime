from django import forms
from django.contrib.auth.models import User 
from django.contrib.auth.forms import UserCreationForm
from .models import Profile , UserProfile
from dashboard.models import stores 


class UserRegisterForm(UserCreationForm): 
    email = forms.EmailField()
    first_name = forms.CharField()
    last_name = forms.CharField() 

    
    class Meta: 
        model = User
        fields = ['username','first_name','last_name','email','password1', 'password2']


class UserProfileForm(forms.ModelForm):
    
    class Meta:
        model = Profile
        fields = ['mobile_Number']

class UserStoreForm(forms.ModelForm): 

    class Meta:
        model = UserProfile
        fields = ['employee_Number', 'store_Number']