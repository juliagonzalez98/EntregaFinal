from django import forms  


class ArticulosForm(forms.Form):
    nombre_titulo = forms.CharField(max_length=80)
    nombre_subtitulo = forms.CharField(max_length=140)

