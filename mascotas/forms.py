from django import forms
from .models import Perro, Gato, Pajaro

class PerroForm(forms.ModelForm):
    class Meta:
        model = Perro
        fields = ['nombre', 'raza', 'sexo']

class GatoForm(forms.ModelForm):
    class Meta:
        model = Gato
        fields = ['nombre', 'raza', 'sexo']

class PajaroForm(forms.ModelForm):
    class Meta:
        model = Pajaro
        fields = ['nombre', 'raza', 'sexo']

class BusquedaForm(forms.Form):
    termino = forms.CharField(max_length=50, required=False, label='Buscar por nombre:') 