from rest_framework import serializers

from hospiApp.models.paciente import Paciente

class PacienteCambiarMedicoSerializer(serializers.ModelSerializer):
    class Meta:
        model = Paciente
        fields = ['medico']