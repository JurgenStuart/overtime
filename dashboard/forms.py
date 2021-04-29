from django import forms
from .models import avlShifts, stores

class createShift(forms.ModelForm): 
    
    class Meta: 
       model = avlShifts
       fields = [ 'shift_Time' , 'shift_Date', 'store_Number']