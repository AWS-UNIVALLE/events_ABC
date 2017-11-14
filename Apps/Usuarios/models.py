from django.db import models
from django.contrib.auth.models import User

# Create your models here.
class Usuario(User):
    cedula=models.CharField(max_length=20, blank=True)
    nombre_usuario = models.CharField(max_length=30,blank=True)
    cargo = models.CharField(max_length=30, blank=True)
<<<<<<< HEAD
    telefono = models.CharField(max_length=30)
    telefono_celular = models.CharField(max_length=30)
=======
    telefono = models.CharField(max_length=100)
    telefono_celular = models.CharField(max_length=100)
>>>>>>> develop
    
    
    
    
    
    