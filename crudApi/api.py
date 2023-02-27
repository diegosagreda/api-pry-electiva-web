#View set establecer quien puede consultar la informacion de la api
from .models import Usuario

from rest_framework import viewsets, permissions
from .serializers import UsuarioSerializer

class UsuarioViewSet(viewsets.ModelViewSet):

    def get_queryset(self):
        return Usuario.objects.all()

    Usuario.objects.all()
    permission_classes = [permissions.AllowAny]
    serializer_class = UsuarioSerializer
