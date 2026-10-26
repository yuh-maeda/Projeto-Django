from django.shortcuts import render
from django.urls import reverse_lazy
from django.views.generic import ListView, CreateView, DeleteView
from hospital.forms import PacienteForm, ExameForm, MedicoForm
from hospital.models import Pacientes, Exames, Medicos

# Create your views here.

# views pacientes
class pacientesListView(ListView):
    model = Pacientes
    template_nome = "hospital/pacientes_list.html"
    context_object_name = "pacientes"
    paginate_by = 5

class pacientesCreateView(CreateView):
    model = Pacientes
    form_class = PacienteForm
    template_name = "hospital/paciente_form_create.html"
    success_url = reverse_lazy("hospital:pacientes_list")

class pacientesDeleteView(DeleteView):
    model = Pacientes
    template_name = "hospital/paciente_confirm_delete.html"
    context_object_name = "pacientes"
    success_url = reverse_lazy("hospital:pacientes_list")

# views exames
class examesListView(ListView):
    model = Exames
    template_nome = "hospital/exames_list.html"
    context_object_name = "exames"

class examesCreateView(CreateView):
    model = Exames
    form_class = ExameForm
    template_name = "hospital/exame_form_create.html"
    success_url = reverse_lazy("hospital:exames_list")

class examesDeleteView(DeleteView):
    model = Exames
    template_name = "hospital/exame_confirm_delete.html"
    context_object_name = "exames"
    success_url = reverse_lazy("hospital:exames_list")

# views medicos
class medicosListView(ListView):
    model = Medicos
    template_nome = "hospital/medicos_list.html"
    context_object_name = "medicos"
    paginate_by = 5

class medicosCreateView(CreateView):
    model = Medicos
    form_class = MedicoForm
    template_name = "hospital/medico_form_create.html"
    success_url = reverse_lazy("hospital:medicos_list")

class medicosDeleteView(DeleteView):
    model = Medicos
    template_name = "hospital/medico_confirm_delete.html"
    context_object_name = "medicos"
    success_url = reverse_lazy("hospital:medicos_list")