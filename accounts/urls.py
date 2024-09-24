from django.urls import path
from .views import *

urlpatterns = [
    path('registro/', user_registro, name='registro'),
    path('login/', user_login, name='login'),
    path('logout/', user_logout, name='logout'),
]