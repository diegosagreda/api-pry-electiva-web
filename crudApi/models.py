from django.db import models

# Create your models here.
class  Usuario(models.Model):
    id = models.AutoField(primary_key=True)
    cedula = models.CharField(max_length=10)
    usuario = models.CharField(max_length=30)
    contrasena = models.CharField(max_length=30)
