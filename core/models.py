from django.db import models
from django.contrib.auth.models import AbstractUser

class Apoderado(models.Model):
    rut = models.CharField('Rut', max_length=10)
    nombre = models.CharField('Nombre', max_length=50)
    apellido = models.CharField('Apellido', max_length=50)
    telefono = models.CharField('Telefono', max_length=9)
    email = models.EmailField('Email', max_length=50)
    direccion = models.CharField('Direccion', max_length=50)
    is_apoderado = models.BooleanField('Es Apoderado', default=False)
    niño = models.ForeignKey('Niño', blank=True, on_delete=models.CASCADE, related_name='niño_del_apoderado')

    def __str__(self):
        return self.nombre

class User(AbstractUser):
    apoderado = models.ForeignKey(Apoderado, on_delete=models.SET_NULL, null=True, blank=True)
    is_parvularia = models.BooleanField('Es Parvularia', default=False)
    is_apoderado = models.BooleanField('Es Apoderado', default=False)

class Niño(models.Model):
    apoderado = models.ForeignKey(Apoderado, on_delete=models.CASCADE, related_name='apoderado_del_niño')
    nombre = models.CharField('Nombre', max_length=50)
    apellido = models.CharField('Apellido', max_length=50)
    edad = models.IntegerField('Edad')
    fecha_nacimiento = models.DateField('Fecha de nacimiento')
    telefono = models.CharField('Telefono', max_length=9)
    email = models.EmailField('Email', max_length=50)
    direccion = models.CharField('Direccion', max_length=50)

    def __str__(self):
        return self.nombre
