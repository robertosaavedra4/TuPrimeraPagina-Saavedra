from django.shortcuts import render, redirect, get_object_or_404
from django.contrib.auth import login, logout, authenticate
from django.contrib.auth.forms import AuthenticationForm
from django.contrib.auth.decorators import login_required
from django.contrib import messages # Para mostrar mensajes al usuario
from .forms import CustomUserCreationForm, UserEditForm, PerfilEditForm
from .models import Perfil
from django.contrib.auth.models import User

def login_view(request):
    if request.user.is_authenticated:
        return redirect('index') # Si ya está logueado, redirige al inicio

    if request.method == 'POST':
        form = AuthenticationForm(request, data=request.POST)
        if form.is_valid():
            username = form.cleaned_data.get('username')
            password = form.cleaned_data.get('password')
            user = authenticate(username=username, password=password)
            if user is not None:
                login(request, user)
                messages.success(request, f"Bienvenido de nuevo, {username}!")
                # Redirigir a la página de donde vino o al index
                next_url = request.POST.get('next', '/')
                return redirect(next_url or 'index')
            else:
                messages.error(request, "Usuario o contraseña incorrectos.")
        else:
            messages.error(request, "Usuario o contraseña incorrectos.")
    else:
        form = AuthenticationForm()

    # Pasar la URL 'next' a la plantilla si existe
    next_url = request.GET.get('next', '')
    return render(request, 'usuarios/login.html', {'form': form, 'next': next_url})


def logout_view(request):
    if request.method == 'POST': # Asegurarse que el logout sea por POST
        logout(request)
        messages.info(request, "Has cerrado sesión exitosamente.")
        return redirect('login')
    # Si se accede por GET, redirigir al inicio o mostrar un error
    return redirect('index')


def registro_view(request):
    if request.user.is_authenticated:
        return redirect('index')

    if request.method == 'POST':
        form = CustomUserCreationForm(request.POST)
        if form.is_valid():
            user = form.save()
            login(request, user) # Loguear al usuario automáticamente después del registro
            messages.success(request, "¡Registro exitoso! Bienvenido.")
            return redirect('index') # Redirigir al inicio
        else:
             # Mostrar errores específicos del formulario si es posible
             for field, errors in form.errors.items():
                 for error in errors:
                     messages.error(request, f"{field}: {error}")
    else:
        form = CustomUserCreationForm()
    return render(request, 'usuarios/registro.html', {'form': form})


@login_required
def ver_perfil_view(request):
    # El perfil se crea automáticamente por la señal, así que debería existir
    # Usamos get_object_or_404 por si acaso algo falló
    perfil = get_object_or_404(Perfil, user=request.user)
    return render(request, 'usuarios/perfil.html', {'perfil': perfil})


@login_required
def editar_perfil_view(request):
    perfil = get_object_or_404(Perfil, user=request.user)

    if request.method == 'POST':
        # Pasamos instance=request.user y instance=perfil para que sean formularios de edición
        user_form = UserEditForm(request.POST, instance=request.user)
        perfil_form = PerfilEditForm(request.POST, request.FILES, instance=perfil) # Añadir request.FILES para la imagen

        if user_form.is_valid() and perfil_form.is_valid():
            user_form.save()
            perfil_form.save()
            messages.success(request, '¡Tu perfil ha sido actualizado exitosamente!')
            return redirect('ver_perfil') # Redirigir a la vista del perfil
        else:
            messages.error(request, 'Por favor corrige los errores.')
            # Mostrar errores específicos si es necesario
            # for field, errors in user_form.errors.items(): messages.error(request, f"User-{field}: {errors}")
            # for field, errors in perfil_form.errors.items(): messages.error(request, f"Perfil-{field}: {errors}")

    else:
        user_form = UserEditForm(instance=request.user)
        perfil_form = PerfilEditForm(instance=perfil)

    return render(request, 'usuarios/editar_perfil.html', {
        'user_form': user_form,
        'perfil_form': perfil_form
    }) 