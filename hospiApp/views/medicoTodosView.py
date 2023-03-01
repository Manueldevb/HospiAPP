from rest_framework import generics,status,views
from rest_framework.response import Response
from rest_framework.views import APIView

from hospiApp.models.medico import Medico
from hospiApp.serializers.medicoSerializer import MedicoSerializer

class MedicoTodosView(generics.ListCreateAPIView):
    queryset = Medico.objects.all()
    serializer_class = MedicoSerializer
    def get(self, request, *args, **kwargs):
        return super().get(request, *args, **kwargs)