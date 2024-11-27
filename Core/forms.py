from django import forms
from .models import Computacion

class computacionForm(forms.ModelForm):
    class Meta:
        model=Computacion
        fields='__all__'