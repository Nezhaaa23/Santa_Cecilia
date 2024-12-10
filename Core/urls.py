from django.contrib.auth.views import LogoutView
from django.urls import path
from django.shortcuts import redirect
from . import views
from .views import CustomLoginView, Base,aseo,computacion,profesores,agregar,modificar,eliminar,agregarA,modificarA,eliminarA,agregarP,modificarP,eliminarP,index,reportes,extraescolar,inteEscolar
urlpatterns = [
    path('', lambda request: redirect('login/')),  
    path('login/', CustomLoginView.as_view(), name='Login'),
    path('logout/', LogoutView.as_view(next_page='/login/'), name='Logout'),
    path('index/',index,name='index'),
    path('base/', Base, name='Base'),
    path('aseo/', aseo, name='aseo'),
    path('agregarA/',agregarA,name='agregarA'),
    path('modificarA/<int:id>/',modificarA,name='modificarA'),
    path('eliminarA/<int:id>/',eliminarA,name='eliminarA'),
    path('computacion/', computacion, name='computacion'),
    path('agregar/',agregar,name='agregar'),
    path('modificar/<int:id>/',modificar,name='modificar'),
    path('eliminar/<int:id>/',eliminar,name='eliminar'),
    path('profesores/', profesores, name='profesores'),
    path('agregarP/',agregarP,name='agregarP'),
    path('modificarP/<int:id>/',modificarP,name='modificarP'),
    path('eliminarP/<int:id>/',eliminarP,name='eliminarP'),
    path('Extraescolar/', extraescolar, name='Extraescolar'),
    path('agregarE/', views.agregarE, name='agregarE'),
    path('modificarE/<int:id>/', views.modificarE, name='modificarE'),
    path('eliminarE/<int:id>/', views.eliminarE, name='eliminarE'),
    path('InteEscolar/', inteEscolar, name='InteEscolar'),
    path('agregarI/', views.agregarI, name='agregarI'),
    path('modificarI/<int:id>/', views.modificarI, name='modificarI'),
    path('eliminarI/<int:id>/', views.eliminarI, name='eliminarI'),
    path('reportes/',reportes,name='reportes'),
    path('descargar_pdf/', views.generar_pdf, name='descargar_pdf'),
    path('descargar_pdf_1/', views.generar_pdf_1, name='descargar_pdf_1'),
    path('descargar_pdf_2/', views.generar_pdf_2, name='descargar_pdf_2'),
    path('descargar_pdf_3/', views.generar_pdf_3, name='descargar_pdf_3'),
    path('descargar_pdf_4/', views.generar_pdf_4, name='descargar_pdf_4'),
    path('descargar_pdf_5/', views.generar_pdf_5, name='descargar_pdf_5'),
]