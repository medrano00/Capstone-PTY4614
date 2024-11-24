from django.urls import path
from .views import *
from django.conf import settings
from django.conf.urls.static import static

handler404 = custom_404
handler500 = custom_500

app_name = 'cursos'

urlpatterns = [
    # URLs - Página Principal y Lógicas de Autenticación #
    path('', index, name='index'),
    path('login/', login_view, name='login'),
    path('logout/', logout_view, name='logout'),
    path('register/', register, name='register'),
    
    # URLs - Portal de Parvularia #
    path('parvularia/', parvularia, name='parvularia'),
    path('parvularia/portalAsistencia/', portalAsistencia.as_view(), name='portalAsistencia'),
    path('parvularia/portalAsistencia/<str:codigo_curso>/estudiantes/', CursoDetailView.as_view(), name='curso'),
    path('parvularia/portalNotas/', portalNotas, name='portalNotas'),
    path('parvularia/portalNotas/agregar/', crearNota, name='crearNota'),
    path('parvularia/portalNotas/editar/<int:id>/', editarNota, name='editarNota'),
    path('parvularia/portalNotas/eliminar/<int:id>/', eliminarNota, name='eliminarNota'),
    path('parvularia/planificaciones/', planificaciones, name='planificaciones'),
    path('parvularia/reportes', reportes, name='reportes'),
    
    # URLs - Portal de Apoderado #
    path('apoderado/', apoderado, name='apoderado'),
    path('apoderado/planificaciones/', planificacionesApoderado, name='planificacionesApoderado'),
    path('apoderado/reportes/', reportesApoderado, name='reportesApoderado'),
    path('apoderado/portalNino/', portalNino, name='portalNino'),
    path('apoderado/resumenNino/<int:id>/', resumenNino, name='resumenNino'),
] + static(settings.STATIC_URL, document_root=settings.STATIC_ROOT)

if settings.DEBUG:
    urlpatterns += static(settings.MEDIA_URL, document_root=settings.MEDIA_ROOT) 