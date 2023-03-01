from rest_framework import generics, status, views
from rest_framework.response import Response

from hospiApp.models.paciente import Paciente
from hospiApp.serializers.pacienteCambiarMedicoSerializer import PacienteCambiarMedicoSerializer

class PacienteCambiarMedicoView(generics.UpdateAPIView):
    queryset = Paciente.objects.all()
    serializer_class = PacienteCambiarMedicoSerializer