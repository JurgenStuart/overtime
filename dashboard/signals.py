from django.db.models.signals import post_save
from users.models import Profile, UserProfile
from django.dispatch import receiver
from .models import stores
from django.contrib.auth.signals import user_logged_in

#@receiver(user_logged_in)
#def loggedUserstore(sender, request, **kwargs): 
    #logged_user = request.UserProfile.store_Number
   # return str(logged_user)