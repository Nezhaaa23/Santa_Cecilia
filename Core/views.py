from django.shortcuts import render,get_object_or_404,redirect
from django.contrib.auth.views import LoginView
from django.urls import reverse_lazy
from .forms import computacionForm,AseoForm,ProfesoresForm
from .models import Computacion,Aseo,Profesores

def aseo(request):
    productos = Aseo.objects.all()
    data = {'productos': productos}
    return render(request, 'Core/aseo.html',data)
def computacion(request):
    productos = Computacion.objects.all()
    data = {'productos': productos}
    return render(request, 'Core/computacion.html',data)
def profesores(request):
    productos = Profesores.objects.all()
    data= {'productos': productos}
    return render(request, 'Core/profesores.html',data)
def Base(request):
    return render(request, 'Core/Base.html')

def listar(request):
    productos = Computacion.objects.all()
    data = {'productos': productos}  # Aquí se usa un diccionario para pasar el contexto
    return render(request, 'Core/crud/Computacion/listar.html', data)

def agregar(request):
    data={'form':computacionForm}
    if request.method == 'POST':
        formulario = computacionForm(data=request.POST,files=request.FILES)
        if formulario.is_valid():
            formulario.save()
            data["mensaje"]="guardado correctamente"
            return redirect('computacion')
        else:
            data["form"]=formulario
    return render(request, 'Core/crud/Computacion/agregar.html',data)

def modificar(request, id):
    producto = get_object_or_404(Computacion, id_material=id)  
    data = {'form': computacionForm(instance=producto)}

    if request.method == 'POST':
        formulario = computacionForm(data=request.POST, instance=producto)
        if formulario.is_valid():
            formulario.save()
            return redirect('computacion')  
        else:
            data["form"] = formulario

    return render(request, 'Core/crud/Computacion/modificar.html', data)

def eliminar(request, id):
    # Usa 'id_material' en lugar de 'id'
    producto = get_object_or_404(Computacion, id_material=id)  
    producto.delete()
    return redirect('computacion')

def agregarA(request):
    data={'form':AseoForm}
    if request.method == 'POST':
        formulario = AseoForm(data=request.POST,files=request.FILES)
        if formulario.is_valid():
            formulario.save()
            data["mensaje"]="guardado correctamente"
            return redirect('aseo')
        else:
            data["form"]=formulario
    return render(request, 'Core/crud/Aseo/agregarA.html',data)

def modificarA(request, id):
    
    producto = get_object_or_404(Aseo, id_insumo=id)  
    data = {'form': AseoForm(instance=producto)}

    if request.method == 'POST':
        formulario = AseoForm(data=request.POST, instance=producto)
        if formulario.is_valid():
            formulario.save()
            return redirect('aseo')  
        else:
            data["form"] = formulario

    return render(request, 'Core/crud/Aseo/modificarA.html', data)

def eliminarA(request, id):
    producto = get_object_or_404(Aseo, id_insumo=id)  
    producto.delete()
    return redirect('aseo')

def agregarP(request):
    data={'form':ProfesoresForm}
    if request.method == 'POST':
        formulario = ProfesoresForm(data=request.POST,files=request.FILES)
        if formulario.is_valid():
            formulario.save()
            data["mensaje"]="guardado correctamente"
            return redirect('profesores')
        else:
            data["form"]=formulario
    return render(request, 'Core/crud/Profesores/agregarP.html',data)

def modificarP(request, id):
    
    producto = get_object_or_404(Profesores, id_objeto=id)  
    data = {'form': ProfesoresForm(instance=producto)}

    if request.method == 'POST':
        formulario = ProfesoresForm(data=request.POST, instance=producto)
        if formulario.is_valid():
            formulario.save()
            return redirect('profesores')  
        else:
            data["form"] = formulario

    return render(request, 'Core/crud/Profesores/modificarP.html', data)

def eliminarP(request, id):
    producto = get_object_or_404(Profesores, id_objeto=id)  
    producto.delete()
    return redirect('profesores')


class CustomLoginView(LoginView):
    template_name = 'Core/Login.html'  
    redirect_authenticated_user = True  
    success_url = reverse_lazy('Base')  