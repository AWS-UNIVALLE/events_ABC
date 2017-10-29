from django.db import models

# Create your models here.
class Noticia(models.Model):
    titulo = models.CharField(max_length=50)
    fechaNoticia= models.DateField()
    contenido = models.TextField()
    imagen = models.CharField(max_length=100)