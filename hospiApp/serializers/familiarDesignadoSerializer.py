from rest_framework import serializers
from hospiApp.models.familiarDesignado import FamiliarDesignado

class FamiliarDesignadoSerializer(serializers.ModelSerializer):
    class Meta:
        model = FamiliarDesignado
        fields = ['id', 'nombre', 'apellido', 'numTelefono', 'genero', 'parentesco', 'correo', 'paciente']