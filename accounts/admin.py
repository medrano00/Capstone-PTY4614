from django.contrib import admin
from .models import User
# Register your models here.

class UserAdmin(admin.ModelAdmin):
    list_display = ['username', 'nombre', 'apellido', 'email', 'telefono']
    search_fields = ['username', 'nombre', 'apellido', 'email']

admin.site.register(User, UserAdmin)