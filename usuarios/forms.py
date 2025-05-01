from django import forms
from django.contrib.auth.forms import UserCreationForm, UserChangeForm
from django.contrib.auth.models import User
from .models import Perfil

class CustomUserCreationForm(UserCreationForm):
    # Puedes añadir campos extra aquí si quieres pedirlos durante el registro
    # email = forms.EmailField(required=True) # Ejemplo: hacer email obligatorio
    class Meta(UserCreationForm.Meta):
        model = User
        fields = UserCreationForm.Meta.fields + ('email', 'first_name', 'last_name',) # Añadir campos al registro

class UserEditForm(forms.ModelForm):
    # No incluimos el password aquí, se maneja por separado
    class Meta:
        model = User
        fields = ['username', 'email', 'first_name', 'last_name']

class PerfilEditForm(forms.ModelForm):
    class Meta:
        model = Perfil
        fields = ['avatar', 'biografia']
        widgets = {
            'biografia': forms.Textarea(attrs={'rows': 4}),
        } 