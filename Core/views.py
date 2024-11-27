from django.shortcuts import render,get_object_or_404,redirect
from django.contrib.auth.views import LoginView
from django.urls import reverse_lazy
from .forms import computacionForm
from .models import Computacion

def aseo(request):
    return render(request, 'Core/aseo.html')
def computacion(request):
    return render(request, 'Core/computacion.html')
def profesores(request):
    return render(request, 'Core/profesores.html')
def Base(request):
    return render(request, 'Core/Base.html')

def agregar(request):
    data={'form':computacionForm}
    if request.method == 'POST':
        formulario = computacionForm(data=request.POST,files=request.FILES)
        if formulario.is_valid():
            formulario.save()
            data["mensaje"]="guardado correctamente"
        else:
            data["form"]=formulario
    return render(request, 'Core/crud/agregar.html',data)

def modificar(request, id):
    # Usa 'id_material' en lugar de 'id'
    producto = get_object_or_404(Computacion, id_material=id)  
    data = {'form': computacionForm(instance=producto)}

    if request.method == 'POST':
        formulario = computacionForm(data=request.POST, instance=producto)
        if formulario.is_valid():
            formulario.save()
            return redirect('Base')  # Redirige a la página principal después de modificar
        else:
            data["form"] = formulario

    return render(request, 'Core/crud/modificar.html', data)

def eliminar(request, id):
    # Usa 'id_material' en lugar de 'id'
    producto = get_object_or_404(Computacion, id_material=id)  
    producto.delete()
    return redirect('Base')

class CustomLoginView(LoginView):
    template_name = 'Core/Login.html'  
    redirect_authenticated_user = True  
    success_url = reverse_lazy('Base')  