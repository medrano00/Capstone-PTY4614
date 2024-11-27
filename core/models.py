from django.db import models
from django.utils import timezone
from django.contrib.auth.models import AbstractUser
from django.core.validators import EmailValidator
from django.core.exceptions import ValidationError

# Modelos Base de la Aplicación
class User(AbstractUser):
    rut = models.CharField('Rut', max_length=12, default='11.111.111-1')
    nombre = models.CharField('Nombre', max_length=50, default='')
    apellido = models.CharField('Apellido', max_length=50, default='')
    edad = models.PositiveIntegerField('Edad', default=1)
    fecha_nacimiento = models.DateField('Fecha de nacimiento', default='1950-01-01')
    telefono = models.CharField('Telefono', max_length=12, default='')
    email = models.EmailField('Email', max_length=50, default='')
    direccion = models.CharField('Direccion', max_length=50, default='')
    is_apoderado = models.BooleanField('Es Apoderado', default=True)
    is_parvularia = models.BooleanField('Es Parvularia', default=False)

    def __str__(self):
        return self.nombre

    class Meta:
        verbose_name = 'Usuario'
        verbose_name_plural = 'Usuarios'

    def save(self, *args, **kwargs):
        if not self.is_apoderado:
            self.is_apoderado = True
        try:
            EmailValidator()(self.email)
            if self.email.endswith('@parvularia.parvuloconnect.cl'):
                self.is_parvularia = True
            else:
                self.is_parvularia = False
        except ValidationError as e:
            print(f"Error al validar el correo: {e}")

        super().save(*args, **kwargs)


class Apoderado(models.Model):
    userApoderado = models.OneToOneField(User, on_delete=models.CASCADE, primary_key=True)

    def __str__(self):
        return self.user.nombre

# Modelos - Portal de Parvularia
class Planificacion(models.Model):
    descripcion = models.CharField(max_length=255)
    documento = models.FileField(upload_to='planificaciones/', default='planificaciones/')
    subido_a = models.DateTimeField(default=timezone.now)

    class Meta:
        verbose_name = 'Planificación de Parvularias'
        verbose_name_plural = 'Planificaciones de Parvularias'

class Reportes(models.Model):
    descripcion = models.CharField(max_length=255)
    documento = models.FileField(upload_to='reportes/', default='reportes/')
    subido_a = models.DateTimeField(default=timezone.now)

    class Meta:
        verbose_name = 'Reporte de Parvularias'
        verbose_name_plural = 'Reportes de Parvularias'

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
        verbose_name = 'Curso'
        verbose_name_plural = 'Cursos'

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
        verbose_name = 'Estudiante'
        verbose_name_plural = 'Estudiantes'

class Asistencia(Base):
    ESTADO_CHOICES = [("P", "Presente"), ("A", "Ausente")]
    estudiante = models.ForeignKey(Estudiante, on_delete=models.CASCADE, related_name="asistencias")
    fecha = models.DateField()
    estado_asistencia = models.CharField(max_length=1, choices=ESTADO_CHOICES)

    def __str__(self):
        return (f"{self.estudiante.nombre} - {self.created} - "f"{self.get_estado_asistencia_display()}")

    class Meta:
        ordering = ["fecha"]
        verbose_name = 'Asistencia'
        verbose_name_plural = 'Asistencias'

class Notas(models.Model):
    NOTAS_CHOICES = [("L", "Logrado"), ("NL", "No Logrado")]
    NIVELES_CHOICES = [("DFM", "Desarrollo Físico y Motor"), ("DSE", "Desarollo Socioemocional"), ("DCG", "Desarrollo Cognitivo"), ("DCM", "Desarrollo Comunicativo")]
    SESIONES_CHOICES = [("1", "Una sesión"), ("2", "Dos sesiones"), ("3", "Tres sesiones"), ("4", "Cuatro sesiones"), ("5", "Cinco sesiones"), ("6", "Seis sesiones"), ("7", "Siete sesiones"), ("8", "Ocho sesiones"), ("9", "Nueve sesiones"), ("10", "Diez sesiones")]
    Estudiante_ID = models.ForeignKey(Estudiante, on_delete=models.CASCADE)
    Curso_ID = models.ForeignKey(Curso, on_delete=models.CASCADE)
    Periodo_ID = models.CharField(max_length=10, default='2020-2021')
    Semestre = models.CharField(max_length=3)
    Nota = models.CharField(max_length=2, choices=NOTAS_CHOICES, default='L')
    Nivel = models.CharField(max_length=3, choices=NIVELES_CHOICES, default='DFM')
    Sesion = models.CharField(max_length=2, choices=SESIONES_CHOICES, default='10')

    def __str__(self):
        return (f"{self.Estudiante_ID.nombre} - {self.Curso_ID.nombre_curso} - {self.get_Nivel_display()} - {self.get_Nota_display()} - {self.get_Sesion_display()}")

    class Meta:
        db_table = "notas"
        verbose_name = 'Nota'
        verbose_name_plural = 'Notas'

class PlanificacionApoderado(models.Model):
    descripcion = models.CharField(max_length=255)
    documento = models.FileField(upload_to='actividades/', default='actividades/')
    subido_a = models.DateTimeField(default=timezone.now)

    class Meta:
        verbose_name = 'Planificación de Apoderados'
        verbose_name_plural = 'Planificaciones de Apoderados'

class ReportesApoderado(models.Model):
    descripcion = models.CharField(max_length=255)
    documento = models.FileField(upload_to='reportesApoderado/', default='reportesApoderado/')
    subido_a = models.DateTimeField(default=timezone.now)

class PlanificacionApoderado(models.Model):
    descripcion = models.CharField(max_length=255)
    documento = models.FileField(upload_to='actividades/', default='actividades/')
    subido_a = models.DateTimeField(default=timezone.now)

    class Meta:
        verbose_name = 'Reporte de Apoderados'
        verbose_name_plural = 'Reportes de Apoderados'