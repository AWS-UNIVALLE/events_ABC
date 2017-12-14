from django.db import models
from Apps.Usuarios.models import Usuario
from Apps.Eventos.models import Evento

class Inscripcion(models.Model):
    estado_inscripcion = models.IntegerField()
    estado_preinscripcion = models.IntegerField()
    estado_pago = models.IntegerField()
    participante = models.ManyToManyField(Usuario)
    evento = models.ForeignKey(Evento, null=True, blank=True)