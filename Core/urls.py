from django.urls import path
from django.shortcuts import redirect  
from .views import CustomLoginView, Base

urlpatterns = [
    path('', lambda request: redirect('login/')),  

    path('login/', CustomLoginView.as_view(), name='Login'),
    
    path('base/', Base, name='Base'),
]