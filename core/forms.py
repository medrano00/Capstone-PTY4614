from django import forms
from django.contrib.auth.forms import UserCreationForm
from .models import User, Planificacion, Asistencia, Estudiante, PlanificacionApoderado, Notas, Reportes, ReportesApoderado

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
    class Meta:
        model = Planificacion
        fields = ["descripcion", "documento", ]

class PlanificacionApoderadoForm(forms.ModelForm):
    class Meta:
        model = PlanificacionApoderado
        fields = ["descripcion", "documento", ]

class ReportesForm(forms.ModelForm):
    class Meta:
        model = Reportes
        fields = ["descripcion", "documento", ]

class ReportesApoderadoForm(forms.ModelForm):
    class Meta:
        model = ReportesApoderado
        fields = ["descripcion", "documento", ]

class AsistenciaForm(forms.ModelForm):
    class Meta:
        model = Asistencia
        fields = ["estudiante", "fecha", "estado_asistencia"]
        widgets = {
            "fecha": forms.DateInput(attrs={"type": "date", "class": "form-control"}),
            "estudiante": forms.Select(attrs={"class": "form-control"}),
            "estado_asistencia": forms.Select(attrs={"class": "form-control"}),
        }

    def __init__(self, *args, **kwargs):
        curso = kwargs.pop('curso')
        super().__init__(*args, **kwargs)
        self.fields['estudiante'].queryset = Estudiante.objects.filter(curso=curso)


    def clean(self):
        cleaned_data = super().clean()
        estudiante = cleaned_data.get("estudiante")
        fecha = cleaned_data.get("fecha")

        if Asistencia.objects.filter(estudiante=estudiante, fecha=fecha).exists():
            raise forms.ValidationError(
                "Ya existe un registro de asistencia para este estudiante "
                "en esta fecha en el mismo curso."
            )
        return cleaned_data

class NotasForm(forms.ModelForm):
    class Meta:
        model = Notas
        fields = ['Estudiante_ID', 'Curso_ID', 'Periodo_ID', 'Semestre', 'Nota', 'Nivel', 'Sesion']
        widgets = {
            'Estudiante_ID': forms.Select(attrs={'class': 'form-control'}),
            'Curso_ID': forms.Select(attrs={'class': 'form-control'}),
            'Periodo_ID': forms.TextInput(attrs={'class': 'form-control'}),
            'Semestre': forms.TextInput(attrs={'class': 'form-control'}),
            'Nota': forms.Select(attrs={'class': 'form-control'}),
            'Nivel': forms.Select(attrs={'class': 'form-control'}),
            'Sesion': forms.Select(attrs={'class': 'form-control'}),
        }