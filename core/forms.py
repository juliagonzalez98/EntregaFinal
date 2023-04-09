from django import forms
from user.views import *  
from core.models import Articulos


class ArticulosForm(forms.Form):
    class Meta:
       model: Articulos
       titulo = forms.CharField(max_length=80, label="Título")
       subtitulo = forms.CharField(max_length=140, label="Indique si se trata de una serie o una película")
       cuerpo = models.TextField()
       autor = models.CharField(max_length=100)
       fecha = models.DateTimeField(auto_now_add=True)
       imagen = models.ImageField(upload_to='media/images/')

    







