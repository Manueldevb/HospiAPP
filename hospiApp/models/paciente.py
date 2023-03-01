from django.db import models
from .persona import Persona
from .medico import Medico

class Paciente(Persona):
    direccion = models.CharField(max_length=50)
    ciudad = models.CharField(max_length=50)
    fechaNacimiento = models.DateTimeField(max_length=50)
    latitud = models.CharField(max_length=50)
    longitud = models.CharField(max_length=50)
    medico = models.ForeignKey(
        Medico,
        on_delete=models.CASCADE,
        blank=True,
        null=True
    )