from rest_framework import serializers
from hospiApp.models.medico import Medico

class MedicoSerializer(serializers.ModelSerializer):
    class Meta:
        model = Medico
        fields = ['id', 'nombre', 'apellido', 'numTelefono', 'genero', 'especialidad', 'registro']