from django.contrib import admin
from .models import User, Apoderado, Niño

@admin.register(User)
class UserAdmin(admin.ModelAdmin):
    list_display = ('username', 'email', 'first_name', 'last_name', 'is_parvularia', 'is_apoderado')
    search_fields = ('username', 'email', 'first_name', 'last_name')
    list_filter = ('is_parvularia', 'is_apoderado')

@admin.register(Apoderado)
class ApoderadoAdmin(admin.ModelAdmin):
    list_display = ('nombre', 'apellido', 'rut', 'telefono', 'email', 'direccion', 'user__is_parvularia', 'user__is_apoderado')
    search_fields = ('nombre', 'apellido', 'rut', 'telefono', 'email', 'direccion')
    list_filter = ('user__is_parvularia', 'user__is_apoderado')

@admin.register(Niño)
class NiñoAdmin(admin.ModelAdmin):
    list_display = ('nombre', 'apellido', 'fecha_nacimiento', 'edad', 'telefono', 'email', 'direccion')
    search_fields = ('nombre', 'apellido', 'fecha_nacimiento', 'edad', 'telefono', 'email', 'direccion')
    list_filter = ('apoderado__user__is_parvularia', 'apoderado__user__is_apoderado')
