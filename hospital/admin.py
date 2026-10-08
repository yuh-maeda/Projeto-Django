from django.contrib import admin
from hospital.models import Medicos, Pacientes, Exames


# Register your models here.
class MedicosAdmin(admin.ModelAdmin):
    list_display = ("nome", "especialidade")
    search_fields = ("nome", "especialidade")

class PacientesAdmin(admin.ModelAdmin):
    list_display = ("nome", "idade")
    search_fields = ("nome",)

class ExameAdmin(admin.ModelAdmin):
    list_display = ("nome", "medico", "paciente", "periodo")
    search_fields = ("nome",)
    list_filter = ("medico", "periodo")

admin.site.register(Medicos, MedicosAdmin)
admin.site.register(Pacientes, PacientesAdmin)
admin.site.register(Exames, ExameAdmin)  