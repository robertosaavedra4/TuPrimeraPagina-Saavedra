from django import forms
from .models import Perro, Gato, Pajaro, Animal

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
    termino = forms.CharField(max_length=100, required=False, label='Buscar por nombre')

class AnimalForm(forms.ModelForm):
    class Meta:
        model = Animal
        fields = ['nombre', 'especie', 'edad', 'descripcion', 'fecha_registro', 'imagen']
        widgets = {
            'fecha_registro': forms.DateInput(attrs={'type': 'date'}),
            'descripcion': forms.Textarea(attrs={'rows': 3}),
        } 