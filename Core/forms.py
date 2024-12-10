from django import forms
from .models import Computacion,Aseo,Profesores, Extraescolar, InteEscolar

class computacionForm(forms.ModelForm):
    class Meta:
        model=Computacion
        fields='__all__'

class AseoForm(forms.ModelForm):
    class Meta:
        model=Aseo
        fields='__all__'

class ProfesoresForm(forms.ModelForm):
    class Meta:
        model=Profesores
        fields='__all__'

class extraescolarForm(forms.ModelForm):
    class Meta:
        model=Extraescolar
        fields='__all__'

class inteescolarForm(forms.ModelForm):
    class Meta:
        model=InteEscolar
        fields='__all__'