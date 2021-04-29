from django import forms
from .models import avlShifts, stores

class createShift(forms.ModelForm): 
    
    class meta: 
       model = avlShifts
       fields = [ 'shift_Time' , 'shift_Date', 'store_Number']