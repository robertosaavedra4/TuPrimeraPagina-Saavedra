from django.shortcuts import render, redirect
from .models import Perro, Gato, Pajaro
from .forms import PerroForm, GatoForm, PajaroForm, BusquedaForm

def index(request):
    return render(request, 'mascotas/index.html')

def perros(request):
    if request.method == 'POST':
        formulario = PerroForm(request.POST)
        if formulario.is_valid():
            formulario.save()
            return redirect('perros')
    else:
        formulario = PerroForm()
    
    perros = Perro.objects.all()
    return render(request, 'mascotas/perros.html', {'form': formulario, 'perros': perros})

def gatos(request):
    if request.method == 'POST':
        formulario = GatoForm(request.POST)
        if formulario.is_valid():
            formulario.save()
            return redirect('gatos')
    else:
        formulario = GatoForm()
    
    gatos = Gato.objects.all()
    return render(request, 'mascotas/gatos.html', {'form': formulario, 'gatos': gatos})

def pajaros(request):
    if request.method == 'POST':
        formulario = PajaroForm(request.POST)
        if formulario.is_valid():
            formulario.save()
            return redirect('pajaros')
    else:
        formulario = PajaroForm()
    
    pajaros = Pajaro.objects.all()
    return render(request, 'mascotas/pajaros.html', {'form': formulario, 'pajaros': pajaros})

def buscar(request):
    resultados = []
    if request.method == 'GET':
        formulario = BusquedaForm(request.GET)
        if formulario.is_valid():
            termino = formulario.cleaned_data.get('termino')
            if termino:
                perros = Perro.objects.filter(nombre__icontains=termino)
                gatos = Gato.objects.filter(nombre__icontains=termino)
                pajaros = Pajaro.objects.filter(nombre__icontains=termino)
                
                for perro in perros:
                    resultados.append({'tipo': 'Perro', 'nombre': perro.nombre, 'raza': perro.raza, 'sexo': perro.sexo})
                for gato in gatos:
                    resultados.append({'tipo': 'Gato', 'nombre': gato.nombre, 'raza': gato.raza, 'sexo': gato.sexo})
                for pajaro in pajaros:
                    resultados.append({'tipo': 'Pájaro', 'nombre': pajaro.nombre, 'raza': pajaro.raza, 'sexo': pajaro.sexo})
    else:
        formulario = BusquedaForm()
    
    return render(request, 'mascotas/buscar.html', {'form': formulario, 'resultados': resultados}) 