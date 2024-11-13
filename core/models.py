from django.db import models
from django.utils import timezone
from django.contrib.auth.models import AbstractUser

class User(AbstractUser):
    rut = models.CharField('Rut', max_length=12, default='11.111.111-1')
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

    def __str__(self):
        return self.user.nombre
    
class Planificacion(models.Model):
    descripcion = models.CharField(max_length=255, blank=True)
    documento = models.FileField(upload_to='planificaciones/', blank=True, null=True)
    subido_a = models.DateTimeField(default=timezone.now)

class PlanificacionApoderado(models.Model):
    descripcion = models.CharField(max_length=255, blank=True)
    documento = models.FileField(upload_to='actividades/', blank=True, null=True)
    subido_a = models.DateTimeField(default=timezone.now)

class Base(models.Model):
    created = models.DateTimeField(auto_now_add=True)
    updated = models.DateTimeField(auto_now=True)

    class Meta:
        abstract = True


class Curso(Base):
    codigo_curso = models.CharField(max_length=20, unique=True)
    nombre_curso = models.CharField(max_length=100)

    class Meta:
        ordering = ["created"]

    def __str__(self):
        return self.nombre_curso


class Estudiante(Base):
    id_estudiante = models.CharField(max_length=20, unique=True)
    nombre = models.CharField(max_length=100)
    curso = models.ForeignKey(Curso, on_delete=models.CASCADE, related_name="estudiantes")

    def __str__(self):
        return self.nombre

    class Meta:
        ordering = ["created"]


class Asistencia(Base):

    ESTADO_CHOICES = [("P", "Presente"), ("A", "Ausente")]

    estudiante = models.ForeignKey(
        Estudiante, on_delete=models.CASCADE, related_name="asistencias"
    )
    fecha = models.DateField()
    estado_asistencia = models.CharField(max_length=1, choices=ESTADO_CHOICES)

    def __str__(self):
        return (
            f"{self.estudiante.nombre} - {self.created} - "
            f"{self.get_estado_asistencia_display()}"
        )

    class Meta:
        ordering = ["fecha"]
