from django.urls import path
from hospital.views import pacientesListView, pacientesCreateView,pacientesUpdateView, examesListView, examesCreateView,examesUpdateView, medicosListView, medicosCreateView,medicosUpdateView

app_name = "hospital"

urlpatterns = [
    path('pacientes/', pacientesListView.as_view(), name="pacientes_list"),
    path("pacientes/novo/", pacientesCreateView.as_view(), name="paciente_create"),
    path("pacientes/<int:pk>/editar/", pacientesUpdateView.as_view(), name="paciente_update"),

    path('exames/', examesListView.as_view(), name="exames_list"),
    path("exames/novo/", examesCreateView.as_view(), name="exame_create"),
    path("exames/<int:pk>/editar/", examesUpdateView.as_view(), name="exame_update"),
    
    path('medicos/', medicosListView.as_view(), name="medicos_list"),
    path("medicos/novo/", medicosCreateView.as_view(), name="medico_create"),
    path("medicos/<int:pk>/editar/", medicosUpdateView.as_view(), name="medicos_update"),
]
 


