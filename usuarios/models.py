from django.db import models
from django.contrib.auth.models import User

class Perfil(models.Model):
    user = models.OneToOneField(User, on_delete=models.CASCADE)
    # first_name, last_name, email ya están en el modelo User
    avatar = models.ImageField(upload_to='avatares/', null=True, blank=True, default='avatares/default.png')
    biografia = models.TextField(blank=True, null=True) # Campo extra a elección

    def __str__(self):
        return f'Perfil de {self.user.username}' 