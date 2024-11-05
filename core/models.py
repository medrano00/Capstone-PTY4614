from django.db import models
from django.contrib.auth.models import AbstractUser

class User(AbstractUser):
    rut = models.CharField('Rut', max_length=10, default='11.111.111-1')
    nombre = models.CharField('Nombre', max_length=50, default='')
    apellido = models.CharField('Apellido', max_length=50, default='')
    edad = models.PositiveIntegerField('Edad', default=1)
    fecha_nacimiento = models.DateField('Fecha de nacimiento', default='1950-01-01')
    telefono = models.CharField('Telefono', max_length=9, default='')
    email = models.EmailField('Email', max_length=50, default='')
    direccion = models.CharField('Direccion', max_length=50, default='')
    is_apoderado = models.BooleanField('Es Apoderado', default=False)
    is_parvularia = models.BooleanField('Es Parvularia', default=False)
    is_niño = models.BooleanField('Es Niño', default=False)

    def __str__(self):
        return self.nombre

class Apoderado(models.Model):
    userApoderado = models.OneToOneField(User, on_delete=models.CASCADE, primary_key=True)
    niñodelApoderado = models.ForeignKey('Niño', on_delete=models.CASCADE)

    def __str__(self):
        return self.user.nombre
    
class Niño(models.Model):
    userNiño = models.OneToOneField(User, on_delete=models.CASCADE, primary_key=True)
    apoderadodelNiño = models.ForeignKey(Apoderado, on_delete=models.CASCADE)
    
    def __str__(self):
        return self.user.nombre
    
class Planificacion(models.Model):
    # Define los campos de tu modelo aquí
    nombre = models.CharField(max_length=100)
    fecha = models.DateField()