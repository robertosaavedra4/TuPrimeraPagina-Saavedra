from django.urls import path
from . import views
from .views import ( # Importar las CBV
    AnimalListView,
    AnimalDetailView,
    AnimalCreateView,
    AnimalUpdateView,
    AnimalDeleteView,
)

urlpatterns = [
    path('', views.index, name='index'),
    path('perros/', views.perros, name='perros'),
    path('gatos/', views.gatos, name='gatos'),
    path('pajaros/', views.pajaros, name='pajaros'),
    path('buscar/', views.buscar, name='buscar'),
    path('animales/', AnimalListView.as_view(), name='animal_list'),
    path('animales/<int:pk>/', AnimalDetailView.as_view(), name='animal_detail'),
    path('animales/nuevo/', AnimalCreateView.as_view(), name='animal_create'),
    path('animales/<int:pk>/editar/', AnimalUpdateView.as_view(), name='animal_update'),
    path('animales/<int:pk>/borrar/', AnimalDeleteView.as_view(), name='animal_delete'),
    path('about/', views.about, name='about'),
] 