from django.db import models
from django.utils import timezone

class Perro(models.Model):
    nombre = models.CharField(max_length=50)
    raza = models.CharField(max_length=50)
    sexo = models.CharField(max_length=10)
    
    def __str__(self):
        return self.nombre

class Gato(models.Model):
    nombre = models.CharField(max_length=50)
    raza = models.CharField(max_length=50)
    sexo = models.CharField(max_length=10)
    
    def __str__(self):
        return self.nombre

class Pajaro(models.Model):
    nombre = models.CharField(max_length=50)
    raza = models.CharField(max_length=50)
    sexo = models.CharField(max_length=10)
    
    def __str__(self):
        return self.nombre

class Animal(models.Model):
    nombre = models.CharField(max_length=100)
    especie = models.CharField(max_length=50)
    edad = models.IntegerField(null=True, blank=True)
    descripcion = models.CharField(max_length=255, blank=True)
    fecha_registro = models.DateField(default=timezone.now)
    imagen = models.ImageField(upload_to='animales/', null=True, blank=True)

    def __str__(self):
        return f"{self.nombre} ({self.especie})"

    class Meta:
        verbose_name = "Animal"
        verbose_name_plural = "Animales" 