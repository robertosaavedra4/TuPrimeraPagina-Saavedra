from django.shortcuts import render, redirect
from django.urls import reverse_lazy # Para CBV success_url
from django.views.generic import ListView, DetailView, CreateView, UpdateView, DeleteView # Vistas genéricas
from django.contrib.auth.mixins import LoginRequiredMixin # Mixin para requerir login en CBV
from django.contrib.auth.decorators import login_required # Decorador para requerir login en FBV
from .models import Perro, Gato, Pajaro, Animal
from .forms import PerroForm, GatoForm, PajaroForm, BusquedaForm, AnimalForm

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
    
    pajaros_list = Pajaro.objects.all()
    return render(request, 'mascotas/pajaros.html', {'form': formulario, 'pajaros': pajaros_list})

def buscar(request):
    resultados = []
    formulario = BusquedaForm(request.GET or None)

    if request.method == 'GET' and formulario.is_valid():
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

    return render(request, 'mascotas/buscar.html', {'form': formulario, 'resultados': resultados})

# --- Vistas para el modelo Animal (CBV) ---

class AnimalListView(ListView):
    model = Animal
    template_name = 'mascotas/animal_list.html'
    context_object_name = 'animales'

class AnimalDetailView(DetailView):
    model = Animal
    template_name = 'mascotas/animal_detail.html'
    context_object_name = 'animal'

class AnimalCreateView(LoginRequiredMixin, CreateView):
    model = Animal
    form_class = AnimalForm
    template_name = 'mascotas/animal_form.html'
    success_url = reverse_lazy('animal_list')

    def form_valid(self, form):
        return super().form_valid(form)

class AnimalUpdateView(LoginRequiredMixin, UpdateView):
    model = Animal
    form_class = AnimalForm
    template_name = 'mascotas/animal_form.html'
    success_url = reverse_lazy('animal_list')

class AnimalDeleteView(LoginRequiredMixin, DeleteView):
    model = Animal
    template_name = 'mascotas/animal_confirm_delete.html'
    success_url = reverse_lazy('animal_list')

# --- Vista "Acerca de mí" (FBV con decorador) ---

@login_required
def about(request):
    return render(request, 'mascotas/about.html') 