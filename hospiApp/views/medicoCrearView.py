from rest_framework import status, views
from rest_framework.response import Response

from hospiApp.serializers.medicoSerializer import MedicoSerializer

class MedicoCrearView(views.APIView):
    def post(self, request, *args, **kwargs):
        serializer = MedicoSerializer(data=request.data)
        serializer.is_valid(raise_exception=True)
        serializer.save()
        return Response({"estado": "Se ha creado el medico"}, status=status.HTTP_201_CREATED)
