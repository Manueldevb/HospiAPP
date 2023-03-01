from rest_framework import status, views
from rest_framework.response import Response

from hospiApp.serializers.pacienteSerializer import PacienteSerializer

class PacienteCrearView(views.APIView):
    def post(self, request, *args, **kwargs):
        serializer = PacienteSerializer(data=request.data)
        serializer.is_valid(raise_exception=True)
        serializer.save()
        return Response({"estado": "Se ha creado el paciente"}, status=status.HTTP_201_CREATED)
