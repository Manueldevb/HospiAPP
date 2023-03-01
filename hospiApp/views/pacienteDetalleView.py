from ast import arg
from rest_framework  import generics, status, views
from rest_framework.response import Response

from hospiApp.models.paciente import Paciente
from hospiApp.serializers.pacienteSerializer import PacienteSerializer

class PacienteDetalleView(generics.RetrieveAPIView):
    queryset = Paciente.objects.all()
    serializer_class = PacienteSerializer

    def get(self, request, *args, **kwargs):
        return super().get(request, *args, **kwargs)