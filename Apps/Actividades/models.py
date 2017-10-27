from django.db import models
from Apps.Eventos.models import Evento

# Create your models here.
class Actividad(models.Model):
    nombre = models.CharField(max_length=50)
    fechaActividad= models.DateField()
    descripcion = models.TextField()
    duracion = models.IntegerField()
    
    evento = models.ForeignKey(Evento)
    
