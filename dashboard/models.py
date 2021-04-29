from django.db import models
from django.contrib.auth.models import User
from django.db.models.signals import post_save
from django.dispatch import receiver
from phone_field import PhoneField
from users.models import Profile, UserProfile

class stores(models.Model): 
    store_Number = models.CharField(primary_key=True,blank=True, max_length=10)
    store_Name = models.CharField(max_length=30)
    store_address = models.CharField(max_length=30)
    store_Contact = PhoneField(blank=False, help_text='Contact number for store')
   
    def __str__(self):
        return self.store_Name

class avlShifts(models.Model):
    shift_ID = models.AutoField(primary_key=True)
    shift_Time = models.CharField (max_length=11)
    shift_Date = models.DateField (null=False, blank=False)
    store_Number = models.ForeignKey(stores,blank=True, on_delete=models.CASCADE)
   
    def __int__(self):
        return self.shift_ID

class wrkShifts(models.Model):
    confimation_number = models.AutoField(primary_key=True)
    shift_ID = models.ForeignKey(avlShifts, on_delete=models.CASCADE)
    

    def __str__(self):
        return self.confimation_number

class penShifts(models.Model):
    shift_ID = models.ForeignKey(avlShifts, on_delete=models.CASCADE)
    shift_Status = models.BooleanField(default=False)
    employee_Number = models.ForeignKey(UserProfile, on_delete=models.CASCADE)

    def __str__(self):
        return self.shift_ID