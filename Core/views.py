from django.shortcuts import render
from django.contrib.auth.views import LoginView
from django.urls import reverse_lazy


def Base(request):
    return render(request, 'Core/Base.html')

class CustomLoginView(LoginView):
    template_name = 'Core/Login.html'  
    redirect_authenticated_user = True  
    success_url = reverse_lazy('Base')  