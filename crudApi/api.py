#View set establecer quien puede consultar la informacion de la api
from .models import Usuario,Solicitud,Recordatorio

from rest_framework import viewsets, permissions
from .serializers import UsuarioSerializer,SolicitudSerializer,RecordatorioSerializer

class UsuarioViewSet(viewsets.ModelViewSet):

    def get_queryset(self):
        return Usuario.objects.all()

    Usuario.objects.all()
    permission_classes = [permissions.AllowAny]
    serializer_class = UsuarioSerializer

class SolicitudViewSet(viewsets.ModelViewSet):

    def get_queryset(self):
        return Solicitud.objects.all()
    
    Solicitud.objects.all()
    permission_classes = [permissions.AllowAny]
    serializer_class = SolicitudSerializer

class RecordatorioViewSet(viewsets.ModelViewSet):

    def get_queryset(self):
        return Recordatorio.objects.all()
    
    Recordatorio.objects.all()
    permission_classes = [permissions.AllowAny]
    serializer_class = RecordatorioSerializer