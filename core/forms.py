from django import forms
from django.contrib.auth.forms import UserCreationForm
from .models import User, Planificacion

class LoginForm(forms.Form):
    username = forms.CharField(widget= forms.TextInput(attrs={"class": "form-control", "placeholder": "Introduce tu Nombre de Usuario"}), label="Nombre de Usuario")
    password = forms.CharField(widget=forms.PasswordInput(attrs={"class": "form-control", "placeholder": "Introduce tu Contraseña"}), label="Contraseña")


class SignUpForm(UserCreationForm):
    username = forms.CharField(widget=forms.TextInput(attrs={"class": "form-control"}))
    nombre = forms.CharField(widget=forms.TextInput(attrs={"class": "form-control"}))
    apellido = forms.CharField(widget=forms.TextInput(attrs={"class": "form-control"}))
    telefono = forms.CharField(widget=forms.TextInput(attrs={"class": "form-control"}))
    password1 = forms.CharField(widget=forms.PasswordInput(attrs={"class": "form-control"}))
    password2 = forms.CharField(widget=forms.PasswordInput(attrs={"class": "form-control"}))
    email = forms.CharField(widget=forms.TextInput(attrs={"class": "form-control"}))

    class Meta:
        model = User
        fields = ('username', 'nombre', 'apellido', 'email', 'telefono', 'password1', 'password2', 'is_parvularia', 'is_apoderado')
    

class PlanificacionForm(forms.ModelForm):
    titulo = forms.CharField(widget=forms.TextInput(attrs={"class": "form-control", "placeholder": "Título de la planificación"}), label="Título")
    fecha = forms.DateField(widget=forms.SelectDateWidget(attrs={"class": "form-control"}), label="Fecha")
    archivo = forms.FileField(widget=forms.ClearableFileInput(attrs={"class": "form-control"}), label="Subir archivo")

    class Meta:
        model = Planificacion  # Asegúrate de tener un modelo Planificacion
        fields = ['titulo', 'fecha', 'archivo']