from django.contrib.auth.views import LogoutView
from django.urls import path
from django.shortcuts import redirect
from .views import CustomLoginView, Base,aseo,computacion,profesores,agregar,modificar,eliminar

urlpatterns = [
    path('', lambda request: redirect('login/')),  
    path('login/', CustomLoginView.as_view(), name='Login'),
    path('base/', Base, name='Base'),
    path('logout/', LogoutView.as_view(next_page='/login/'), name='Logout'),
    path('aseo/', aseo, name='aseo'),
    path('agregar/',agregar,name='agregar'),
    path('modificar/<int:id>/',modificar,name='modificar'),
    path('eliminar/<int:id>/',eliminar,name='eliminar'),
    path('computacion/', computacion, name='computacion'),
    path('profesores/', profesores, name='profesores'),
]