from rest_framework import generics, status, views
from rest_framework.response import Response

from hospiApp.models.signoVital import SignoVital
from hospiApp.serializers.signoVitalSerializer import SignoVitalSerializer

class SignoVitalTodosView(generics.ListCreateAPIView):
    queryset = SignoVital.objects.all()
    serializer_class = SignoVitalSerializer
    def get(self, request, *args, **kwargs):
        return super().get(request, *args, **kwargs)