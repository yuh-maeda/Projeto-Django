from django.urls import path
from hospital.views import pacientesListView, pacientesCreateView, examesListView, examesCreateView, medicosListView, medicosCreateView

app_name = "hospital"

urlpatterns = [
    path('pacientes/', pacientesListView.as_view(), name="pacientes_list"),
    path("pacientes/novo/", pacientesCreateView.as_view(), name="paciente_create"),

    path('exames/', examesListView.as_view(), name="exames_list"),
    path("exames/novo/", examesCreateView.as_view(), name="exame_create"),
    
    path('medicos/', medicosListView.as_view(), name="medicos_list"),
    path("medicos/novo/", medicosCreateView.as_view(), name="medico_create"),
]