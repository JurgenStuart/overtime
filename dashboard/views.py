from django.shortcuts import render
from .models import avlShifts, stores
from django.contrib.auth.decorators import login_required
from users.models import UserProfile
from .forms import createShift
#from .signals import loggedUserstore

@login_required
def home(request):
    context = {
        'Shifts' : avlShifts.objects.all() 
    }
    return render(request, 'dashboard/home.html', context)

@login_required
def showstores(request): 
    context = { 
        'stores': stores.objects.all()
    }
    return render(request,'dashboard/stores.html', context)

@login_required
def createShift(request): 
    if request.method == 'POST'
    
