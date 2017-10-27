from django.db import models
from Apps.Actividades.models import Actividad
from django.contrib.auth.models import User

# Create your models here.
class Participante(User):
    cedula = models.IntegerField()
    
class Asistencia(models.Model):
    confirmacion = models.CharField(max_length=20)
    actividad = models.ManyToManyField(Actividad)
    participante = models.ForeignKey(Participante, null=True, blank=True)
