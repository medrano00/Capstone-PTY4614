from typing import Any
from django.shortcuts import render, redirect, get_object_or_404
from .forms import SignUpForm, LoginForm, AsistenciaForm, PlanificacionForm, PlanificacionApoderadoForm, ReportesForm, ReportesApoderadoForm
from django.contrib.auth import authenticate, login, logout
from django.http import HttpResponse
from .models import *
from django.views.defaults import page_not_found
from django.conf import settings
from django.contrib import messages
from django.core.files.storage import FileSystemStorage
from django.views.generic.list import ListView
from django.views.generic.detail import DetailView
from django.core.paginator import Paginator, EmptyPage, PageNotAnInteger

# Create your views here.

# Vistas - Página Principal y Lógicas de Autenticación

def index(request):
    return render(request, 'core/index.html')

def register(request):
    msg = None
    if request.method == 'POST':
        form = SignUpForm(request.POST)
        if form.is_valid():
            user = form.save()
            msg = 'Usuario creado'
            return redirect('login')
        else:
            msg = 'Formulario invalido'
    else:
        form = SignUpForm()
    return render(request, 'core/register.html', {'form': form, 'msg': msg})

def login_view(request):
    form = LoginForm(request.POST or None)
    msg = None
    if request.method == 'POST':
        if form.is_valid():
            username = form.cleaned_data.get('username')
            password = form.cleaned_data.get('password')
            user = authenticate(username=username, password=password)
            if user is not None and user.is_parvularia:
                login(request, user)
                return redirect('core:index')
            elif user is not None and user.is_apoderado:
                login(request, user)
                return redirect('core:index')
            elif user is not None and user.is_superuser:
                login(request, user)
                return redirect('core:index')
            else:
                msg = 'Usuario o contraseña incorrectos'
        else:
            msg = 'Formulario invalido'
    return render(request, 'core/login.html', {'form': form, 'msg': msg})


def logout_view(request):
    logout(request)
    return redirect('core:index')

def custom_404(request, exception):
    return render(request, '404.html', status=404)

def custom_500(request):
    return render(request, '500.html', status=500)


# Vistas - Portal de Parvularia 

def parvularia(request):
    if request.user.is_parvularia:
        return render(request, 'core/parvularia.html')
    else:
        return render(request, 'core/403.html', status=403)
        

class portalAsistencia(ListView):
    model = Curso
    template_name = 'core/portalAsistencia.html'

    def get_context_data(self, **kwargs):
        context = super().get_context_data(**kwargs)
        context['object_list'] = self.object_list.order_by('-created')
        return context


class CursoDetailView(DetailView):
    model = Curso
    template_name = "core/portalAsistenciaDetail.html"
    context_object_name = "curso"

    def get_object(self):
        codigo_curso = self.kwargs["codigo_curso"]
        return get_object_or_404(Curso, codigo_curso=codigo_curso)

    def get_context_data(self, **kwargs):
        context = super().get_context_data(**kwargs)

        search_query = self.request.GET.get("q", "")
        date_filter = self.request.GET.get("date", "")
        estado_filter = self.request.GET.get("estado", "")

        try:
            asistencias = Asistencia.objects.filter(estudiante__curso=self.object)

            if search_query:
                asistencias = asistencias.filter(estudiante__nombre__icontains=search_query)
            if date_filter:
                asistencias = asistencias.filter(fecha=date_filter)
            if estado_filter:
                asistencias = asistencias.filter(estado_asistencia=estado_filter)

            paginator = Paginator(asistencias, 10)
            page = self.request.GET.get("page")
            try:
                asistencias_paginadas = paginator.page(page)
            except PageNotAnInteger:
                asistencias_paginadas = paginator.page(1)
            except EmptyPage:
                asistencias_paginadas = paginator.page(paginator.num_pages)

            context["asistencias"] = asistencias_paginadas
            context["form"] = AsistenciaForm(curso=self.object)
            context["paginator"] = paginator
        except Exception as e:
            messages.error(self.request, f"Error al cargar asistencias: {str(e)}")

        return context

    def post(self, request, *args, **kwargs):
        self.object = self.get_object()

        asistencia_id = request.POST.get("asistencia_id")
        if asistencia_id:
            try:
                asistencia = get_object_or_404(Asistencia, id=asistencia_id)
                estado_asistencia = request.POST.get("estado_asistencia")
                asistencia.estado_asistencia = estado_asistencia
                asistencia.save()
                messages.success(request, "Estado de asistencia actualizado exitosamente.")
                return redirect(request.path)
            except Exception as e:
                messages.error(request, f"Error al actualizar asistencia: {str(e)}")
        else:
            try:
                form = AsistenciaForm(request.POST, curso=self.object)
                if form.is_valid():
                    form.save()
                    messages.success(request, "Asistencia registrada exitosamente.")
                    return redirect(request.path)
                else:
                    context = self.get_context_data(object=self.object)
                    context["form"] = form
                    return self.render_to_response(context)
            except Exception as e:
                messages.error(request, f"Error al registrar nueva asistencia: {str(e)}")

        return self.get(request, *args, **kwargs)


def planificaciones(request):
    if request.method == 'POST':
        form = PlanificacionForm(request.POST, request.FILES)
        if form.is_valid():
            form.save()
            return redirect('core:planificaciones')
    else:
        form = PlanificacionForm()

    if request.user.is_parvularia:
        archivos = PlanificacionApoderado.objects.all()
        return render(request, 'core/planificaciones.html', {'form': form, 'archivos': archivos})
    else:
        return render(request, 'core/403.html', status=403)

# Vistas - Portal de Apoderado

def apoderado(request):
    if request.user.is_apoderado:
        return render(request, 'core/apoderado.html')
    else:
        return render(request, 'core/403.html', status=403)

def reportes(request):
    if request.method == 'POST':
        form = ReportesForm(request.POST, request.FILES)
        if form.is_valid():
            form.save()
            return redirect('core:reportes')
    else:
        form = ReportesForm()

    if request.user.is_parvularia:
        reportes = ReportesApoderado.objects.all()
        return render(request, 'core/reportes.html', {'form': form, 'reportes': reportes})
    else:
        return render(request, 'core/403.html', status=403)


def planificacionesApoderado(request):
    if request.method == 'POST':
        form = PlanificacionApoderadoForm(request.POST, request.FILES)
        if form.is_valid():
            form.save()
            return redirect('core:planificacionesApoderado')
    else:
        form = PlanificacionApoderadoForm()

    if request.user.is_apoderado:
        archivos = Planificacion.objects.all()
        return render(request, 'core/planificacionesApoderado.html', {'form': form, 'archivos': archivos})
    else:
        return render(request, 'core/403.html', status=403)


def reportesApoderado(request):
    if request.method == 'POST':
        form = ReportesApoderadoForm(request.POST, request.FILES)
        if form.is_valid():
            form.save()
            return redirect('core:reportesApoderado')
    else:
        form = ReportesApoderadoForm()

    if request.user.is_apoderado:
        reportes = Reportes.objects.all()
        return render(request, 'core/reportesApoderado.html', {'form': form, 'reportes': reportes})
    else:
        return render(request, 'core/403.html', status=403)