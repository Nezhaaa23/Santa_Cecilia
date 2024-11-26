from django.shortcuts import render
from django.contrib.auth.views import LoginView
from django.urls import reverse_lazy
from .views import CustomLoginView, Base,aseo,computacion,profesores
def aseo(request):
    return render(request, 'Core/aseo.html')
def computacion(request):
    return render(request, 'Core/computacion.html')
def profesores(request):
    return render(request, 'Core/profesores.html')
def Base(request):
    return render(request, 'Core/Base.html')

class CustomLoginView(LoginView):
    template_name = 'Core/Login.html'  
    redirect_authenticated_user = True  
    success_url = reverse_lazy('Base')  