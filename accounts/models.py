from django.db import models

class User(models.Model):
    username = models.CharField(max_length=100, default='')
    nombre = models.CharField(max_length=100)
    apellido = models.CharField(max_length=100)
    email = models.EmailField(unique=True)
    telefono = models.CharField(max_length=15)
    password = models.CharField(max_length=100)

    def __str__(self):
        return self.username