from django.shortcuts import render
from django.views.generic import ListView
from hospital.models import Pacientes, Exames, Medicos

# Create your views here.
class pacienteListView(ListView):
    model = Pacientes
    template_nome = "hospital/pacientes_list.html"
    context_object_name = "pacientes"
    paginate_by = 5

class examesListView(ListView):
    model = Exames
    template_nome = "hospital/exames_list.html"
    context_object_name = "exames"

class medicosListView(ListView):
    model = Medicos
    template_nome = "hospital/medicos_list.html"
    context_object_name = "medicos"
    paginate_by = 5