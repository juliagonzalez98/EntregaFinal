from django import forms  
from django.contrib.auth.models import UserCreationForm

class ArticulosForm(forms.Form):
    nombre_titulo = forms.CharField(max_length=80)
    nombre_subtitulo = forms.CharField(max_length=140)

class UserRegisterForm(UserCreationForm):
    pass