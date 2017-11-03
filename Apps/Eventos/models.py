from django.db import models
from Apps.Usuarios.models import Usuario
# Create your models here.
class Evento(models.Model):
    nombre = models.CharField(max_length=50)
    fechaEvento = models.DateField()
    descripcion = models.TextField()
    duracion = models.IntegerField()
    estado = models.CharField(max_length=50)

    def __str__(self):
        return '{}'.format(self.nombre)
        
class Inscripcion(models.Model):
    estado_inscripcion = models.CharField(max_length=30, blank=True)
    estado_pago = models.CharField(max_length=30, blank=True)
    participante = models.ManyToManyField(Usuario)
    evento = models.ForeignKey(Evento, null=True, blank=True)
    