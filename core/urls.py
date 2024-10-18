from django.urls import path
from . import views
from django.conf import settings
from django.conf.urls.static import static
from django.views.defaults import page_not_found

handler404 = page_not_found

urlpatterns = [
    path('', views.index, name= 'index'),
    path('login/', views.login_view, name='login'),
    path('logout/', views.logout_view, name='logout'),
    path('register/', views.register, name='register'),
    path('parvularia/', views.parvularia, name='parvularia'),
    path('apoderado/', views.apoderado, name='apoderado'),
    path('apoderado/perfilNiño/', views.perfilNiño, name='perfilNiño'),
] + static(settings.STATIC_URL, document_root=settings.STATIC_ROOT)