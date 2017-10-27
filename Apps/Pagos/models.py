from django.db import models
from Apps.Eventos.models import Evento
from Apps.Participantes.models import Participante

# Create your models here.
class Pago(models.Model):
    cantidadPago= models.IntegerField()
    estadoPago = models.CharField(max_length=20)
    estadoInscripcion = models.CharField(max_length=20)

    evento = models.OneToOneField(Evento)
    participante = models.OneToOneField(Participante, null=True, blank=True)
