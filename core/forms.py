from django import forms
from user.views import *  
from core.models import Articulos
from django.core.validators import FileExtensionValidator

class ArticulosForm(forms.Form):
    
       titulo = forms.CharField(max_length=80, label="Título")
       subtitulo = forms.CharField(max_length=140, label="Indique si se trata de una serie o una película")
       cuerpo = forms.CharField(widget=forms.Textarea, label="Ingrese una breve reseña del contenido elegido")
       autor = forms.CharField(max_length=100)
       fecha = forms.DateTimeField()
       imagen = forms.FileField(required=False, validators=[FileExtensionValidator(allowed_extensions=['jpg', 'jpeg', 'png', 'gif'])], label="Imagen")

    







