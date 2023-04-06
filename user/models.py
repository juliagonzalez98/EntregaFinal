from django.db import models
from django.contrib.auth.models import User
from django.contrib.auth.mixins import LoginRequiredMixin


# Create your models here.

class Avatar(models.Model):
    user = models.ForeignKey(User, on_delete=models.CASCADE)
    imagen = models.ImageField(upload_to='avatares', null=True, blank=True)

    def __str__(self):
        return f"{self.user} - {self.imagen}"
