from django.db import models
from .persona import Persona

class Medico(Persona):
    especialidad = models.CharField(max_length=50)
    registro = models.CharField(max_length=50)
