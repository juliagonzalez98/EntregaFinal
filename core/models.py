from django.db import models
from django.urls import reverse

# Create your models here.

class Articulos(models.Model):
    titulo = models.CharField(max_length=100)
    subtitulo = models.CharField(max_length=140, default="")
    cuerpo = models.TextField(default="")
    autor = models.CharField(max_length=100, default="")
    fecha = models.DateTimeField(auto_now_add=True, null=True, blank=True)
    imagen = models.ImageField(upload_to='images/', null=True, blank=True)

   
    def __str__(self):
        return f"{self.id} - {self.titulo}"
    

    