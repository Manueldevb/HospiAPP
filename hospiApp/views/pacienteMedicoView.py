from rest_framework import generics, status, views
from rest_framework.response import Response

from hospiApp.models.paciente import Paciente
from hospiApp.serializers.pacienteSerializer import PacienteSerializer

class PacienteMedicoView(generics.ListAPIView):
    serializer_class = PacienteSerializer

    def get(self, request, *args, **kwargs):
        return super().get(request, *args, **kwargs)

    def get_queryset(self):
        medicoid = self.kwargs['medico']
        return Paciente.objects.filter(medico = medicoid)