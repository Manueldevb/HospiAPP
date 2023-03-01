from rest_framework import generics, status, views
from rest_framework.response import Response

from hospiApp.models.familiarDesignado import FamiliarDesignado
from hospiApp.serializers.familiarDesignadoSerializer import FamiliarDesignadoSerializer

class FamiliarDesignadoTodosView(generics.ListCreateAPIView):
    queryset = FamiliarDesignado.objects.all()
    serializer_class = FamiliarDesignadoSerializer
    def get(self, request, *args, **kwargs):
        return super().get(request, *args, **kwargs)