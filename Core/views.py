from django.shortcuts import render
from django.contrib.auth.views import LoginView
from django.urls import reverse_lazy

# Vista base
def Base(request):
    return render(request, 'Core/Base.html')

# Clase para personalizar el formulario de login
class CustomLoginView(LoginView):
    template_name = 'Core/Login.html'  # Ruta del formulario de login
    redirect_authenticated_user = True  # Si el usuario ya está autenticado, redirige a base
    success_url = reverse_lazy('Base')  # Redirige a 'Base' después del login exitoso