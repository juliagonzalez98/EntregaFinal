from django.db import models

# Create your models here.

class Articulos(models.Model):
    titulo = models.CharField(max_length=80)

    def __str__(self):
        return f"{self.id} - {self.titulo}"
    