from django import forms  
from django.contrib.auth.models

class ArticulosForm(forms.Form):
    nombre_titulo = forms.CharField(max_length=80)
    nombre_subtitulo = forms.CharField(max_length=140)
