from django.contrib.auth.views import LogoutView
from django.urls import path
from django.shortcuts import redirect
from .views import CustomLoginView, Base,aseo,computacion,profesores,agregar,modificar,eliminar,listar,agregarA,modificarA,eliminarA,agregarP,modificarP,eliminarP
urlpatterns = [
    path('', lambda request: redirect('login/')),  
    path('login/', CustomLoginView.as_view(), name='Login'),
    path('base/', Base, name='Base'),
    path('logout/', LogoutView.as_view(next_page='/login/'), name='Logout'),
    path('aseo/', aseo, name='aseo'),
    path('agregar/',agregar,name='agregar'),
    path('agregarA/',agregarA,name='agregarA'),
    path('agregarP/',agregarP,name='agregarP'),
    path('listar/',listar,name="listar"),
    path('modificar/<int:id>/',modificar,name='modificar'),
    path('modificarA/<int:id>/',modificarA,name='modificarA'),
    path('modificarP/<int:id>/',modificarP,name='modificarP'),
    path('eliminar/<int:id>/',eliminar,name='eliminar'),
    path('eliminarA/<int:id>/',eliminarA,name='eliminarA'),
    path('eliminarP/<int:id>/',eliminarP,name='eliminarP'),
    path('computacion/', computacion, name='computacion'),
    path('profesores/', profesores, name='profesores'),
]