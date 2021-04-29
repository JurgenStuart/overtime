from django.urls import path
from .import views 


urlpatterns = [
    path('', views.home, name='dashboard-home'),
    path('stores/', views.showstores, name='dashboard-stores'),
    
   
]
