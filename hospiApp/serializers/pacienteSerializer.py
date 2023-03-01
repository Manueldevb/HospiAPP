from rest_framework import serializers
from hospiApp.models.paciente import Paciente

class PacienteSerializer(serializers.ModelSerializer):
    class Meta:
        model = Paciente
        fields = ['id', 'nombre', 'apellido', 'numTelefono', 'genero', 'direccion', 'ciudad', 'fechaNacimiento', 'latitud', 'longitud']
