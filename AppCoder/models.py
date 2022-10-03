from django.db import models
from django.contrib.auth.models import User

# Create your models here.

class Curso(models.Model):

    def __str__(self):

        return f"Nombre: {self.nombre} ------- Camada: {self.camada}"

    nombre = models.CharField(max_length=60)
    camada = models.IntegerField()

class Estudiante(models.Model):

    nombre = models.CharField(max_length=60)
    apellido = models.CharField(max_length=60)
    correo = models.EmailField()

class Profesor(models.Model):
    nombre = models.CharField(max_length=60)
    apellido = models.CharField(max_length=60)
    email = models.EmailField()
    profesion = models.CharField(max_length=60)  

class Entregable(models.Model):
    nombre = models.CharField(max_length=60)
    fechaEntrega = models.DateField()

class Avatar(models.Model):
    usuario = models.ForeignKey(User, on_delete=models.CASCADE)
    imagen = models.ImageField(upload_to="avatares", null=True, blank=True)