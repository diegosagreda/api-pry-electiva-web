from django.db import models

# Create your models here.
class  Usuario(models.Model):
    id = models.AutoField(primary_key=True)
    cedula = models.CharField(max_length=10)
    usuario = models.CharField(max_length=30)
    contrasena = models.CharField(max_length=30)

class Solicitud(models.Model):
    id = models.AutoField(primary_key=True)
    nombre = models.CharField(max_length=100)
    paciente = models.CharField(max_length=100)
    formula = models.CharField(max_length=100)
    fecha = models.DateField(auto_now_add=True)
    estado = models.BooleanField(default=False)
