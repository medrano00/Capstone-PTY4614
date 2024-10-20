from django.urls import path
from .views import *
from django.conf import settings
from django.conf.urls.static import static
from django.conf.urls import handler404, handler500

handler404 = custom_404
handler500 = custom_500

urlpatterns = [
    path('', index, name= 'index'),
    path('login/', login_view, name='login'),
    path('logout/', logout_view, name='logout'),
    path('register/', register, name='register'),
    path('parvularia/', parvularia, name='parvularia'),
    path('apoderado/', apoderado, name='apoderado'),
    path('apoderado/perfilNiño/', perfilNiño, name='perfilNiño'),
] + static(settings.STATIC_URL, document_root=settings.STATIC_ROOT)