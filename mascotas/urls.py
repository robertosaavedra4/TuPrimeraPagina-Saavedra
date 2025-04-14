from django.urls import path
from . import views

urlpatterns = [
    path('', views.index, name='index'),
    path('perros/', views.perros, name='perros'),
    path('gatos/', views.gatos, name='gatos'),
    path('pajaros/', views.pajaros, name='pajaros'),
    path('buscar/', views.buscar, name='buscar'),
] 