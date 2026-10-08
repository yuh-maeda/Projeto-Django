from django.db import models


class Medicos(models.Model):
    nome = models.CharField(verbose_name="Nome", max_length=30)
    especialidade = models.CharField(verbose_name="Especialidade", max_length=50)

    class Meta:
        verbose_name = "Medico"
        verbose_name_plural = "Medicos"
        ordering = ["nome"]

    def __str__(self):
        return f"{self.nome} {self.especialidade}"

class Pacientes(models.Model):
    nome = models.CharField(verbose_name="Nome", max_length=30)
    idade = models.IntegerField(verbose_name="Idade")

    class Meta:
        verbose_name = "Paciente"
        verbose_name_plural = "Pacientes"
        ordering = ["nome"]

    def __str__(self):
        return f"{self.nome} {self.idade}"

class Exames(models.Model):
    escolherPeriodo = [
        ("M", "Matutino"),
        ("V", "Vespertino"),
        ("N", "Noturno"),
    ]

    nome = models.CharField(verbose_name="Nome do exame", max_length=100)
    descricao = models.TextField(verbose_name="Descrição", blank=True)
    periodo = models.CharField(
        verbose_name="Período",
        max_length=1,
        choices=escolherPeriodo,
        default="M",
    )
    medico = models.ForeignKey(
        Medicos,
        on_delete=models.CASCADE,
        verbose_name="Medico Responsável",
    )
    paciente = models.ForeignKey(
        Pacientes,
        on_delete=models.CASCADE,
        verbose_name="Paciente",
    )

    class Meta:
        verbose_name = "Exame"
        verbose_name_plural = "Exames"
        ordering = ["paciente"]

    def __str__(self):
        return self.nome