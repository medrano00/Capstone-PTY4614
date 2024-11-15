from django.contrib import admin
from .models import User, Estudiante, Curso, Asistencia, Planificacion, PlanificacionApoderado, Notas, Reportes, ReportesApoderado

# Register your models here.

class UserAdmin(admin.ModelAdmin):
    list_display = ('rut', 'edad', 'telefono', 'email', 'direccion', 'is_apoderado', 'is_parvularia')
    search_fields = ('rut', 'email')
    list_filter = ('is_apoderado', 'is_parvularia')

class AsistenciaInline(admin.TabularInline):
    model = Asistencia
    fields = ["fecha", "estado_asistencia"]
    can_delete = True
    extra = 1


class BaseAdmin(admin.ModelAdmin):
    readonly_fields = ("created", "updated")

    class Meta:
        abstract = True


class CursoAdmin(BaseAdmin):
    list_display = ("nombre_curso", "codigo_curso")


class EstudianteAdmin(BaseAdmin):
    list_display = ("nombre", "curso")
    inlines = [AsistenciaInline]

class PlanificacionAdmin(admin.ModelAdmin):
    list_display = ("descripcion", "documento", "subido_a")

class PlanificacionApoderadoAdmin(admin.ModelAdmin):
    list_display = ("descripcion", "documento", "subido_a")

class ReportesAdmin(admin.ModelAdmin):
    list_display = ("descripcion", "documento", "subido_a")

class ReportesApoderadoAdmin(admin.ModelAdmin):
    list_display = ("descripcion", "documento", "subido_a")

admin.site.register(User, UserAdmin)
admin.site.register(Curso, CursoAdmin)
admin.site.register(Estudiante, EstudianteAdmin)
admin.site.register(Planificacion, PlanificacionAdmin)
admin.site.register(PlanificacionApoderado, PlanificacionApoderadoAdmin)
admin.site.register(Reportes, ReportesAdmin)
admin.site.register(ReportesApoderado, ReportesApoderadoAdmin)
admin.site.register(Notas)