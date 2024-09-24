from django import forms

class FormRegistro(forms.Form):
    username = forms.CharField(label='Usuario', max_length=100)
    nombre = forms.CharField(label='Nombre', max_length=100)
    apellido = forms.CharField(label='Apellido', max_length=100)
    email = forms.EmailField(label='Email')
    telefono = forms.CharField(label='Teléfono', max_length=100)
    password = forms.CharField(label='Contraseña', widget=forms.PasswordInput())
    password2 = forms.CharField(label='Confirmar contraseña', widget=forms.PasswordInput())
    
class FormLogin(forms.Form):
    username = forms.CharField(label='Usuario', max_length=100)
    password = forms.CharField(label='Contraseña', max_length=100, widget=forms.PasswordInput)