from django.db import models

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