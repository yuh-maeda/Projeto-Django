from django import forms
from hospital.models import Pacientes, Exames, Medicos


class PacienteForm(forms.ModelForm):
    class Meta:
        model = Pacientes
        fields = ["nome", "idade"]

class ExameForm(forms.ModelForm):
    class Meta:
        model = Exames
        fields = ["nome", "descricao", "medico", "paciente", "periodo"]

class MedicoForm(forms.ModelForm):
    class Meta:
        model = Medicos
        fields = ["nome", "especialidade"]