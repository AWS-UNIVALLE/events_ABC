from django.db import models

# Create your models here.
class Evento(models.Model):
    nombre = models.CharField(max_length=100)
    fechaEvento = models.DateField()
    descripcion = models.TextField()
    duracion = models.IntegerField()
    estado = models.CharField(max_length=50)

    def __str__(self):
        return '{}'.format(self.nombre)
        
