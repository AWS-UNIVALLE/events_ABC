from django.db import models
from Apps.Eventos.models import Evento
from Apps.Usuarios.models import Usuario
# Create your models here.

class Actividad(models.Model):
    nombre = models.CharField(max_length=50)
    fechaActividad= models.DateField()
    descripcion = models.TextField()
    duracion = models.IntegerField()
    
    evento = models.ForeignKey(Evento)

class Asistencia(models.Model):
    confirmacion = models.CharField(max_length=30)
    actividad = models.ManyToManyField(Actividad)
    participante = models.ForeignKey(Usuario, null=True, blank=True)