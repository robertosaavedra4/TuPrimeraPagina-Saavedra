from django.db.models.signals import post_save
from django.contrib.auth.models import User
from django.dispatch import receiver
from .models import Perfil

@receiver(post_save, sender=User)
def crear_o_actualizar_perfil(sender, instance, created, **kwargs):
    if created:
        Perfil.objects.create(user=instance)
    else:
        # Si el usuario ya existía, nos aseguramos que tenga perfil
        # Esto es útil si añades el sistema de perfiles a usuarios existentes
        Perfil.objects.get_or_create(user=instance)
        # Guardamos el perfil por si acaso (aunque get_or_create no lo modifica si ya existe)
        # instance.perfil.save() # Descomentar si necesitas forzar guardado en actualizaciones 