from django.db import models
from Apps.Usuarios.models import Usuario

# Create your models here.
class Evento(models.Model):
    nombre = models.CharField(max_length=50)
    fechaEvento = models.DateField()
    descripcion = models.TextField()
    duracion = models.IntegerField()
    estado = models.CharField(max_length=50)

    usuario = models.ForeignKey(Usuario, null=True, blank=True)
    
    def __str__(self):
        return '{}'.format(self.nombre)
