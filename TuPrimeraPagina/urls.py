from django.contrib import admin
from django.urls import path, include
from django.conf import settings # Importar settings
from django.conf.urls.static import static # Importar static

urlpatterns = [
    path('admin/', admin.site.urls),
    path('usuarios/', include('usuarios.urls')), # Incluir URLs de la app usuarios
    path('', include('mascotas.urls')), # Incluir URLs de la app mascotas (raíz)
]

# Servir archivos multimedia en modo DEBUG
if settings.DEBUG:
    urlpatterns += static(settings.MEDIA_URL, document_root=settings.MEDIA_ROOT)
    # Opcional: Servir archivos estáticos si no usas Whitenoise u otro método en producción
    # urlpatterns += static(settings.STATIC_URL, document_root=settings.STATIC_ROOT) 