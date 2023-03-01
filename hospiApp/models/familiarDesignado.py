from django.db import models
from .persona import Persona
from .paciente import Paciente

class FamiliarDesignado(Persona):
    parentesco = models.CharField(max_length=20, default="")
    correo = models.CharField(max_length=50, default="")
    paciente = models.OneToOneField(
        Paciente,
        on_delete=models.CASCADE,
        unique=False,
        blank=True,
        null=True
    )