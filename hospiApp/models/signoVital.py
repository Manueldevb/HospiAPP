from django.db import models

from .paciente import Paciente

class SignoVital(models.Model):
    oximetria = models.FloatField()
    frecuenciaRespiratoria = models.FloatField()
    frecuenciaCardiaca = models.FloatField()
    temperatura = models.FloatField()
    presionArterial = models.FloatField()
    glicemia = models.FloatField()
    fechaRegistro = models.DateTimeField(auto_now_add=True)
    paciente = models.ForeignKey(
        Paciente,
        on_delete = models.CASCADE,
        unique = False,
        blank=True,
        null=True
    )