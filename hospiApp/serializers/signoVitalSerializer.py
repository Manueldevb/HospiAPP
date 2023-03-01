from pyexpat import model
from rest_framework import serializers

from hospiApp.models.signoVital import SignoVital

class SignoVitalSerializer(serializers.ModelSerializer):
    class Meta:
        model = SignoVital
        fields = ['oximetria', 'frecuenciaRespiratoria', 'frecuenciaCardiaca', 'temperatura', 'presionArterial', 'glicemia', 'paciente']