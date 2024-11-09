from django.urls import path
from .views import *
from django.conf import settings
from django.conf.urls.static import static
from django.conf.urls import handler404, handler500

handler404 = custom_404
handler500 = custom_500

urlpatterns = [
    path('', index, name='index'),
    path('login/', login_view, name='login'),
    path('logout/', logout_view, name='logout'),
    path('register/', register, name='register'),
    path('parvularia/', parvularia, name='parvularia'),
    path('parvularia/portalAsistencia/', portalAsistencia, name='portalAsistencia'),
    path('parvularia/portalNotas/', portalNotas, name='portalNotas'),
    path('parvularia/planificaciones/', planificaciones, name='planificaciones'),
    path('guardarAsistencia/', guardarAsistencia, name='guardarAsistencia'),
    path('guardarNotas/', guardarNotas, name='guardarNotas'),
    path('apoderado/', apoderado, name='apoderado'),
    path('apoderado/perfilNiño/', perfilNiño, name='perfilNiño'),
    path('apoderado/planificaciones/', planificacionesApoderado, name='planificacionesApoderado'),
] + static(settings.STATIC_URL, document_root=settings.STATIC_ROOT)

if settings.DEBUG:
    urlpatterns += static(settings.MEDIA_URL, document_root=settings.MEDIA_ROOT) 