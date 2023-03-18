from django.db import models

# Create your models here.
class  Usuario(models.Model):
    id = models.AutoField(primary_key=True)
    nombre = models.CharField(default='',max_length=200)
    cedula = models.CharField(max_length=10)
    usuario = models.CharField(max_length=30)
    contrasena = models.CharField(max_length=30)
    tipo = models.CharField(default='cliente', max_length=30)

class Solicitud(models.Model):
    id = models.AutoField(primary_key=True)
    nombre = models.CharField(max_length=100)
    paciente = models.CharField(max_length=100)
    formula = models.CharField(max_length=500)
    fecha = models.DateField(auto_now_add=True)
    estado = models.BooleanField(default=False)

class Recordatorio(models.Model):
    id = models.AutoField(primary_key=True)
    paciente = models.CharField(max_length=100)
    medicamento = models.CharField(max_length=100)
    intensidad = models.CharField(max_length=100)
    cantidad = models.CharField(max_length=100)
    descripcion = models.CharField(default='',max_length=100)
    estado = models.BooleanField(default=False)

class Reporte(models.Model):
    id = models.AutoField(primary_key=True)
    paciente = models.CharField(max_length=100)
    medicamento = models.CharField(max_length=100)
    cantidad = models.CharField(max_length=100)
    fecha = models.CharField(max_length=100)
    hora = models.CharField(max_length=100)
    estado = models.CharField(max_length=100)