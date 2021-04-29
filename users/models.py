from django.db import models
from django.contrib.auth.models import User
from phone_field import PhoneField
from django.dispatch import receiver
from django.db.models.signals import post_save



class Profile(models.Model): 
    user = models.OneToOneField(User, on_delete=models.CASCADE) 
    mobile_Number = PhoneField(default= ' ', help_text='Contact number for employee')
    
    def __str__(self):
        return f'{self.user.username} Profile'
        
    @receiver(post_save, sender=User)
    def create_profile(sender, instance, created, **kwargs): 
        if created: 
            Profile.objects.create(user=instance)


    @receiver(post_save, sender=User)
    def save_profile(sender, instance, **kwargs):
        instance.profile.save()

    
class UserProfile(models.Model): 
    store_Number = models.ForeignKey("dashboard.stores",default=None, null=True, on_delete=models.CASCADE)
    employee_Number = models.CharField(primary_key=True, max_length=10)
    
    def __str__(self):
        return self.employee_Number
    