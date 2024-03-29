from rest_framework import serializers

from .models import Usuario
from .models import Solicitud
from .models import Recordatorio
from .models import Reporte

class UsuarioSerializer(serializers.ModelSerializer):
    class Meta:
        model = Usuario
        #Campos hacer consultados
        fields = ('id', 'nombre','cedula', 'usuario', 'contrasena','tipo')

        #Para restringir los campos
        #read_only_fields = ('id')
class SolicitudSerializer(serializers.ModelSerializer):
    class Meta:
        model = Solicitud
        fields = ('id', 'nombre','paciente', 'formula', 'fecha', 'estado',)

class RecordatorioSerializer(serializers.ModelSerializer):
    class Meta:
        model = Recordatorio
        fields = ('id','paciente', 'medicamento', 'intensidad', 'cantidad','descripcion','estado')

class ReporteSerializer(serializers.ModelSerializer):
    class Meta:
        model = Reporte
        fields = ('id','paciente', 'medicamento', 'cantidad', 'fecha','hora', 'estado')