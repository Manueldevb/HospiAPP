from django.db import models

class Persona(models.Model):
    id = models.CharField(primary_key=True, max_length=20)
    nombre = models.CharField(max_length=50)
    apellido = models.CharField(max_length=50)
    numTelefono = models.CharField(max_length=20)
    genero = models.CharField(max_length=20)

    class Meta:
        abstract = True