from django.shortcuts import render, get_object_or_404, redirect
from django.contrib.auth.views import LoginView
from django.contrib.staticfiles import finders
from django.urls import reverse_lazy
from .forms import computacionForm, AseoForm, ProfesoresForm, extraescolarForm,inteescolarForm
from .models import Computacion, Aseo, Profesores,Extraescolar,InteEscolar
from django.http import HttpResponse
from reportlab.lib.pagesizes import letter
from reportlab.pdfgen import canvas
from django.contrib import messages


def reportes(request):
    """
    Vista que maneja la página de reportes. Obtiene los objetos de Aseo, Computación y Profesores
    del modelo y los pasa al template para su visualización.
    """
    aseo = Aseo.objects.all()
    computacion = Computacion.objects.all()
    profesores = Profesores.objects.all()
    inteescolar=InteEscolar.objects.all()
    extraescolar=Extraescolar.objects.all()

    data = {
        'aseo': aseo,
        'computacion': computacion,
        'profesores': profesores,
        'inteescolar':inteescolar,
        'extraescolar':extraescolar
    }
    return render(request, 'Core/reportes.html', data)

def index(request):
    return render(request, 'Core/index.html')

def aseo(request):
    """
    Vista que maneja la página de productos de aseo. Obtiene todos los productos de aseo
    del modelo y los pasa al template para su visualización.
    """
    productos = Aseo.objects.all()
    data = {'productos': productos}
    return render(request, 'Core/aseo.html', data)

def computacion(request):
    """
    Vista que maneja la página de productos de computación. Obtiene todos los productos de computación
    del modelo y los pasa al template para su visualización.
    """
    productos = Computacion.objects.all()
    data = {'productos': productos}
    return render(request, 'Core/computacion.html', data)

def profesores(request):
    """
    Vista que maneja la página de productos de profesores. Obtiene todos los productos de profesores
    del modelo y los pasa al template para su visualización.
    """
    productos = Profesores.objects.all()
    data = {'productos': productos}
    return render(request, 'Core/profesores.html', data)

def Base(request):
    """
    Vista que maneja la página base.
    """
    return render(request, 'Core/Base.html')

def inteEscolar(request):
    productos = InteEscolar.objects.all()
    data = {'productos': productos}
    return render(request,'Core/InteEscolar.html',data)

def extraescolar(request):
    productos = Extraescolar.objects.all()
    data = {'productos': productos}
    return render(request,'Core/Extraescolar.html',data)

def agregar(request):
    """
    Vista que maneja la funcionalidad de agregar un nuevo producto de computación.
    Utiliza el formulario computacionForm para capturar los datos del nuevo producto.
    """
    data = {'form': computacionForm}
    if request.method == 'POST':
        formulario = computacionForm(data=request.POST, files=request.FILES)
        if formulario.is_valid():
            formulario.save()
            messages.success(request, 'Se agrego correctamente')
            return redirect('computacion')
        else:
            data["form"] = formulario
    return render(request, 'Core/crud/Computacion/agregar.html', data)

def modificar(request, id):
    """
    Vista que maneja la funcionalidad de modificar un producto de computación existente.
    Utiliza el formulario computacionForm para capturar los datos actualizados del producto.
    """
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
    """
    Vista que maneja la funcionalidad de eliminar un producto de computación.
    Utiliza el id_material del producto para identificarlo y eliminarlo del modelo.
    """
    producto = get_object_or_404(Computacion, id_material=id)
    producto.delete()
    return redirect('computacion')

def agregarA(request):
    """
    Vista que maneja la funcionalidad de agregar un nuevo producto de aseo.
    Utiliza el formulario AseoForm para capturar los datos del nuevo producto.
    """
    data = {'form': AseoForm}
    if request.method == 'POST':
        formulario = AseoForm(data=request.POST, files=request.FILES)
        if formulario.is_valid():
            formulario.save()
            messages.success(request, 'Se agrego correctamente')
            return redirect('aseo')
        else:
            data["form"] = formulario
    return render(request, 'Core/crud/Aseo/agregarA.html', data)

def modificarA(request, id):
    """
    Vista que maneja la funcionalidad de modificar un producto de aseo existente.
    Utiliza el formulario AseoForm para capturar los datos actualizados del producto.
    """
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
    """
    Vista que maneja la funcionalidad de eliminar un producto de aseo.
    Utiliza el id_insumo del producto para identificarlo y eliminarlo del modelo.
    """
    producto = get_object_or_404(Aseo, id_insumo=id)
    producto.delete()
    return redirect('aseo')

def agregarP(request):
    """
    Vista que maneja la funcionalidad de agregar un nuevo producto de profesores.
    Utiliza el formulario ProfesoresForm para capturar los datos del nuevo producto.
    """
    data = {'form': ProfesoresForm}
    if request.method == 'POST':
        formulario = ProfesoresForm(data=request.POST, files=request.FILES)
        if formulario.is_valid():
            formulario.save()
            messages.success(request, 'Se agrego correctamente')
            return redirect('profesores')
        else:
            data["form"] = formulario
    return render(request, 'Core/crud/Profesores/agregarP.html', data)

def modificarP(request, id):
    """
    Vista que maneja la funcionalidad de modificar un producto de profesores existente.
    Utiliza el formulario ProfesoresForm para capturar los datos actualizados del producto.
    """
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
    """
    Vista que maneja la funcionalidad de eliminar un producto de profesores.
    Utiliza el id_objeto del producto para identificarlo y eliminarlo del modelo.
    """
    producto = get_object_or_404(Profesores, id_objeto=id)
    producto.delete()
    return redirect('profesores')

def agregarI(request):

    data = {'form': inteescolarForm}
    if request.method == 'POST':
        formulario = inteescolarForm(data=request.POST, files=request.FILES)
        if formulario.is_valid():
            formulario.save()
            messages.success(request, 'Se agrego correctamente')
            return redirect('InteEscolar')
        else:
            data["form"] = formulario
    return render(request, 'Core/crud/InteEscolar/agregarI.html', data)

def modificarI(request,id):
    producto = get_object_or_404(InteEscolar, id_inteescolar=id)
    data = {'form': inteescolarForm(instance=producto)}

    if request.method == 'POST':
        formulario = inteescolarForm(data=request.POST, instance=producto)
        if formulario.is_valid():
            formulario.save()
            return redirect('InteEscolar')
        else:
            data["form"] = formulario

    return render(request, 'Core/crud/InteEscolar/modificarI.html', data)    

def eliminarI(request,id):
    producto = get_object_or_404(InteEscolar, id_inteescolar=id)
    producto.delete()
    return redirect('InteEscolar')

def agregarE(request):

    data = {'form': extraescolarForm}
    if request.method == 'POST':
        formulario = extraescolarForm(data=request.POST, files=request.FILES)
        if formulario.is_valid():
            formulario.save()
            messages.success(request, 'Se agrego correctamente')
            return redirect('Extraescolar')
        else:
            data["form"] = formulario
    return render(request, 'Core/crud/Extraescolar/agregarE.html', data)

def modificarE(request,id):
    producto = get_object_or_404(Extraescolar, id_extraescolar=id)
    data = {'form': extraescolarForm(instance=producto)}

    if request.method == 'POST':
        formulario = extraescolarForm(data=request.POST, instance=producto)
        if formulario.is_valid():
            formulario.save()
            return redirect('Extraescolar')
        else:
            data["form"] = formulario

    return render(request, 'Core/crud/Extraescolar/modificarE.html', data)

def eliminarE(request,id):
    producto = get_object_or_404(Extraescolar, id_extraescolar=id)
    producto.delete()
    return redirect('Extraescolar')

def generar_pdf(request):
    """
    Genera un reporte PDF con información de los productos de aseo, computación y profesores,
    asegurando que el contenido no choque con el logo.
    """
    # Crear una respuesta HttpResponse con el tipo de contenido como PDF
    response = HttpResponse(content_type='application/pdf')
    response['Content-Disposition'] = 'attachment; filename="reporte.pdf"'
    
    # Crear el objeto Canvas para dibujar el PDF
    p = canvas.Canvas(response, pagesize=letter)
    width, height = letter  # Obtén el tamaño de la página
    
    # Agregar el logotipo (ajustar posición y tamaño)
    logo_path = finders.find('Core/img/logo.jpg')
    logo_width = 100
    logo_height = 100
    logo_x = 50
    logo_y = height - logo_height - 20
    if logo_path:
        p.drawImage(logo_path, logo_x, logo_y, width=logo_width, height=logo_height)
    else:
        print("Logo no encontrado.")

    
    margin_top = logo_y - 20  


    p.setFont("Helvetica-Bold", 16)
    p.drawString(logo_x + logo_width + 20, margin_top + 30, "Reporte de Productos")  # Alinear a la derecha del logo


    y_position = margin_top - 20

 
    p.setFont("Helvetica-Bold", 12)
    p.drawString(100, y_position, "Productos de Aseo")
    y_position -= 20
    aseo = Aseo.objects.all()
    for producto in aseo:
        if y_position < 40:  # Salto de página si no hay espacio suficiente
            p.showPage()
            y_position = height - 40
        p.setFont("Helvetica", 10)
        p.drawString(100, y_position, f"Nombre: {producto.nombre_insumo}, Tipo: {producto.tipo_insumo}, Cantidad: {producto.cantidad_insumo}")
        y_position -= 20

  
    p.setFont("Helvetica-Bold", 12)
    p.drawString(100, y_position - 20, "Productos de Computación")
    y_position -= 40
    computacion = Computacion.objects.all()
    for producto in computacion:
        if y_position < 40:  # Salto de página si no hay espacio suficiente
            p.showPage()
            y_position = height - 40
        p.setFont("Helvetica", 10)
        p.drawString(100, y_position, f"Nombre: {producto.nombre_material}, Tipo: {producto.tipo_material}, Cantidad: {producto.cantidad_material}")
        y_position -= 20

   
    p.setFont("Helvetica-Bold", 12)
    p.drawString(100, y_position - 20, "Productos de Profesores")
    y_position -= 40
    profesores = Profesores.objects.all()
    for producto in profesores:
        if y_position < 40:  # Salto de página si no hay espacio suficiente
            p.showPage()
            y_position = height - 40
        p.setFont("Helvetica", 10)
        p.drawString(100, y_position, f"Nombre: {producto.nombre_objeto}, Tipo: {producto.tipo_producto}, Cantidad: {producto.cantidad_objeto}")
        y_position -= 20
   
    p.setFont("Helvetica-Bold", 12)
    p.drawString(100, y_position, "Productos de Extra escolares")
    y_position -= 20
    extraescolar = Extraescolar.objects.all()
    for producto in extraescolar:
        if y_position < 40:  # Salto de página si no hay espacio suficiente
            p.showPage()
            y_position = height - 40
        p.setFont("Helvetica", 10)
        p.drawString(100, y_position, f"Nombre: {producto.nombre_extraescolar}, Tipo: {producto.tipo_extraescolar}, Cantidad: {producto.cantidad_extraescolar}")
        y_position -= 20
    
    p.setFont("Helvetica-Bold", 12)
    p.drawString(100, y_position, "Productos de Inte escolar")
    y_position -= 20
    inteescolar = InteEscolar.objects.all()
    for producto in inteescolar:
        if y_position < 40:  # Salto de página si no hay espacio suficiente
            p.showPage()
            y_position = height - 40
        p.setFont("Helvetica", 10)
        p.drawString(100, y_position, f"Nombre: {producto.nombre_inteescolar}, Tipo: {producto.tipo_inteescolar}, Cantidad: {producto.cantidad_inteescolar}")
        y_position -= 20

    # Finalizar el PDF
    p.showPage()
    p.save()    
    
    return response

def generar_pdf_1(request):

    response = HttpResponse(content_type='application/pdf')
    response['Content-Disposition'] = 'attachment; filename="Reporte_Aseo.pdf"'
    
    p = canvas.Canvas(response, pagesize=letter)
    width, height = letter 
    
    logo_path = finders.find('Core/img/logo.jpg')
    logo_width = 100
    logo_height = 100
    logo_x = 50
    logo_y = height - logo_height - 20
    if logo_path:
        p.drawImage(logo_path, logo_x, logo_y, width=logo_width, height=logo_height)
    else:
        print("Logo no encontrado.")

    
    margin_top = logo_y - 20  


    p.setFont("Helvetica-Bold", 16)
    p.drawString(logo_x + logo_width + 20, margin_top + 30, "Reporte de Aseo") 


    y_position = margin_top - 20

 
    p.setFont("Helvetica-Bold", 12)
    p.drawString(100, y_position, "")
    y_position -= 20
    aseo = Aseo.objects.all()
    for producto in aseo:
        if y_position < 40:
            p.showPage()
            y_position = height - 40
        p.setFont("Helvetica", 10)
        p.drawString(100, y_position, f"Nombre: {producto.nombre_insumo}, Tipo: {producto.tipo_insumo}, Cantidad: {producto.cantidad_insumo}")
        y_position -= 20

    # Finalizar el PDF
    p.showPage()
    p.save()    
    
    return response

def generar_pdf_2(request):

    response = HttpResponse(content_type='application/pdf')
    response['Content-Disposition'] = 'attachment; filename="Reporte_Computacion.pdf"'
    
    p = canvas.Canvas(response, pagesize=letter)
    width, height = letter 
    
    logo_path = finders.find('Core/img/logo.jpg')
    logo_width = 100
    logo_height = 100
    logo_x = 50
    logo_y = height - logo_height - 20
    if logo_path:
        p.drawImage(logo_path, logo_x, logo_y, width=logo_width, height=logo_height)
    else:
        print("Logo no encontrado.")

    
    margin_top = logo_y - 20  


    p.setFont("Helvetica-Bold", 16)
    p.drawString(logo_x + logo_width + 20, margin_top + 30, "Reporte de Computacion") 


    y_position = margin_top - 20

    p.setFont("Helvetica-Bold", 12)
    p.drawString(100, y_position - 20, "")
    y_position -= 20
    computacion = Computacion.objects.all()
    for producto in computacion:
        if y_position < 40:  
            p.showPage()
            y_position = height - 40
        p.setFont("Helvetica", 10)
        p.drawString(100, y_position, f"Nombre: {producto.nombre_material}, Tipo: {producto.tipo_material}, Cantidad: {producto.cantidad_material}")
        y_position -= 20

    p.showPage()
    p.save()    
    
    return response

def generar_pdf_3(request):

    response = HttpResponse(content_type='application/pdf')
    response['Content-Disposition'] = 'attachment; filename="Reporte_Profesores.pdf"'
    
    p = canvas.Canvas(response, pagesize=letter)
    width, height = letter 
    
    logo_path = finders.find('Core/img/logo.jpg')
    logo_width = 100
    logo_height = 100
    logo_x = 50
    logo_y = height - logo_height - 20
    if logo_path:
        p.drawImage(logo_path, logo_x, logo_y, width=logo_width, height=logo_height)
    else:
        print("Logo no encontrado.")

    
    margin_top = logo_y - 20  


    p.setFont("Helvetica-Bold", 16)
    p.drawString(logo_x + logo_width + 20, margin_top + 30, "Reporte de Profesores") 


    y_position = margin_top - 20

    p.setFont("Helvetica-Bold", 12)
    p.drawString(100, y_position - 20, "")
    y_position -= 40
    profesores = Profesores.objects.all()
    for producto in profesores:
        if y_position < 40:  # Salto de página si no hay espacio suficiente
            p.showPage()
            y_position = height - 40
        p.setFont("Helvetica", 10)
        p.drawString(100, y_position, f"Nombre: {producto.nombre_objeto}, Tipo: {producto.tipo_producto}, Cantidad: {producto.cantidad_objeto}")
        y_position -= 20
    

    p.showPage()
    p.save()    

    return response

def generar_pdf_4(request):
    
    response = HttpResponse(content_type='application/pdf')
    response['Content-Disposition'] = 'attachment; filename="Reporte_Extra_escolares.pdf"'
    
    p = canvas.Canvas(response, pagesize=letter)
    width, height = letter 
    
    logo_path = finders.find('Core/img/logo.jpg')
    logo_width = 100
    logo_height = 100
    logo_x = 50
    logo_y = height - logo_height - 20
    if logo_path:
        p.drawImage(logo_path, logo_x, logo_y, width=logo_width, height=logo_height)
    else:
        print("Logo no encontrado.")

    
    margin_top = logo_y - 20  


    p.setFont("Helvetica-Bold", 16)
    p.drawString(logo_x + logo_width + 20, margin_top + 30, "Reporte de Extra escolares") 


    y_position = margin_top - 20

     
    p.setFont("Helvetica-Bold", 12)
    p.drawString(100, y_position, "")
    y_position -= 20
    extraescolar = Extraescolar.objects.all()
    for producto in extraescolar:
        if y_position < 40:  
            p.showPage()
            y_position = height - 40
        p.setFont("Helvetica", 10)
        p.drawString(100, y_position, f"Nombre: {producto.nombre_extraescolar}, Tipo: {producto.tipo_extraescolar}, Cantidad: {producto.cantidad_extraescolar}")
        y_position -= 20
    

    p.showPage()
    p.save()   

    return response

def generar_pdf_5(request):

    response = HttpResponse(content_type='application/pdf')
    response['Content-Disposition'] = 'attachment; filename="Reporte_Extra_escolares.pdf"'
    
    p = canvas.Canvas(response, pagesize=letter)
    width, height = letter 
    
    logo_path = finders.find('Core/img/logo.jpg')
    logo_width = 100
    logo_height = 100
    logo_x = 50
    logo_y = height - logo_height - 20
    if logo_path:
        p.drawImage(logo_path, logo_x, logo_y, width=logo_width, height=logo_height)
    else:
        print("Logo no encontrado.")

    
    margin_top = logo_y - 20  


    p.setFont("Helvetica-Bold", 16)
    p.drawString(logo_x + logo_width + 20, margin_top + 30, "Reporte de Extra escolares") 


    y_position = margin_top - 20

     
    p.setFont("Helvetica-Bold", 12)
    p.drawString(100, y_position, "Productos de Inte escolar")
    y_position -= 20
    inteescolar = InteEscolar.objects.all()
    for producto in inteescolar:
        if y_position < 40:  # Salto de página si no hay espacio suficiente
            p.showPage()
            y_position = height - 40
        p.setFont("Helvetica", 10)
        p.drawString(100, y_position, f"Nombre: {producto.nombre_inteescolar}, Tipo: {producto.tipo_inteescolar}, Cantidad: {producto.cantidad_inteescolar}")
        y_position -= 20
    

    p.showPage()
    p.save()   

    return response

class CustomLoginView(LoginView):
    template_name = 'Core/Login.html'  
    redirect_authenticated_user = True  
    success_url = reverse_lazy('Base')  