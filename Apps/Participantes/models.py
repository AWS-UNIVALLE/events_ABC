from django.db import models
from Apps.Actividades.models import Actividad
from django.contrib.auth.models import User

# Create your models here.
class Participante(User):
    cedula = models.IntegerField()
    
    
    
