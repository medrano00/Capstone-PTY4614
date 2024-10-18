from django.contrib import admin
from .models import User

# Register your models here.

class UserAdmin(admin.ModelAdmin):
    list_display = ('rut', 'edad', 'telefono', 'email', 'direccion', 'is_apoderado', 'is_parvularia', 'is_niño')
    search_fields = ('rut', 'email')
    list_filter = ('is_apoderado', 'is_parvularia', 'is_niño')

admin.site.register(User, UserAdmin)