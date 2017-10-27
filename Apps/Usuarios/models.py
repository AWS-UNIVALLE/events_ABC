from django.db import models
from django.contrib.auth.models import User

# Create your models here.
class Usuario(User):
    #nombre = models.CharField(max_length=20)
    #apellidos = models.CharField(max_length=30, null=True)
    cedula = models.IntegerField()
    #correo = models.EmailField()
    telefono = models.IntegerField()
    estado = models.CharField(max_length=50, default='Activo')
    cargo = models.CharField(default='Operador',max_length=20)
