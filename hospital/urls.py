from django.urls import path
from hospital.views import pacienteListView, examesListView, medicosListView

app_name = "hospital"

urlpatterns = [
    path('pacientes/', pacienteListView.as_view(), name="pacientes_list"),
    path('exames/', examesListView.as_view(), name="exames_list"),
    path('medicos/', medicosListView.as_view(), name="medicos_list"),
]