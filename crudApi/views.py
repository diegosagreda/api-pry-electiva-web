from urllib import response
from django.shortcuts import render

from .models import Usuario

def iniciarSesion(request):
    usuario = request.POST['usuario']
    constrasena = request.POST['contrasena']

    sesion = Usuario.objects.filter(usuario=usuario,contrasena=constrasena)

    if sesion :
        return response({'sesion': 'true'})
    else:
        return response({'sesion': 'false'})