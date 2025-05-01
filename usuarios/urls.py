from django.urls import path
# Importa las vistas de Django Auth directamente si prefieres usarlas
# from django.contrib.auth import views as auth_views
from . import views

urlpatterns = [
    # Usamos nuestras vistas personalizadas
    path('login/', views.login_view, name='login'),
    path('logout/', views.logout_view, name='logout'),
    path('registro/', views.registro_view, name='registro'),
    path('perfil/', views.ver_perfil_view, name='ver_perfil'),
    path('perfil/editar/', views.editar_perfil_view, name='editar_perfil'),

    # Si quisieras usar las vistas de Django para login/logout:
    # path('login/', auth_views.LoginView.as_view(template_name='usuarios/login.html'), name='login'),
    # path('logout/', auth_views.LogoutView.as_view(next_page='login'), name='logout'), # next_page es opcional aquí si lo tienes en settings
] 