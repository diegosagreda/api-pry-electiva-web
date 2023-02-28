from rest_framework import serializers

from .models import Usuario
from .models import Solicitud

class UsuarioSerializer(serializers.ModelSerializer):
    class Meta:
        model = Usuario
        #Campos hacer consultados
        fields = ('id', 'cedula', 'usuario', 'contrasena')

        #Para restringir los campos
        #read_only_fields = ('id')
class SolicitudSerializer(serializers.ModelSerializer):
    class Meta:
        model: Solicitud
        fields = ('id', 'nombre','paciente', 'formula', 'fecha', 'estado')
                  