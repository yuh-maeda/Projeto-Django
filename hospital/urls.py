from django.urls import path
from hospital.views import pacientesListView, pacientesCreateView, pacientesUpdateView, pacientesDeleteView, examesListView, examesCreateView, examesUpdateView, examesDeleteView, medicosListView, medicosCreateView, medicosUpdateView, medicosDeleteView

app_name = "hospital"

urlpatterns = [
    path("pacientes/", pacientesListView.as_view(), name="pacientes_list"),
    path("pacientes/novo/", pacientesCreateView.as_view(), name="paciente_create"),
    path("pacientes/<int:pk>/editar/", pacientesUpdateView.as_view(), name="paciente_update"),
    path("pacientes/<int:pk>/excluir/", pacientesDeleteView.as_view(), name="paciente_delete"),

    path("exames/", examesListView.as_view(), name="exames_list"),
    path("exames/novo/", examesCreateView.as_view(), name="exame_create"),
    path("exames/<int:pk>/editar/", examesUpdateView.as_view(), name="exame_update"),
    path("exames/<int:pk>/excluir/", examesDeleteView.as_view(), name="exame_delete"),
    
    path('medicos/', medicosListView.as_view(), name="medicos_list"),
    path("medicos/novo/", medicosCreateView.as_view(), name="medico_create"),
    path("medicos/<int:pk>/editar/", medicosUpdateView.as_view(), name="medicos_update"),
    path("medicos/<int:pk>/excluir/", medicosDeleteView.as_view(), name="medico_delete"),
]   
