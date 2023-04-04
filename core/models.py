from django.db import models
from django.urls import reverse

# Create your models here.

class Articulos(models.Model):
    titulo = models.CharField(max_length=100)
    subtitulo = models.CharField(max_length=140, default="")
    #contenido = models.TextField(max_length=1400)


    def __str__(self):
        return f"{self.id} - {self.titulo}"
    