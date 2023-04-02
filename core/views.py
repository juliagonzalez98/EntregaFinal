from django.shortcuts import render
from core.models import Articulos
from core.forms import ArticulosForm


# Create your views here.

def inicio(request):
    return render(request, 'core/index.html')

def muestra_articulos(request): 

    articulosx = Articulos.objects.all()
    
    return render (request, 'core/mostrar_articulos.html', {"articulos": articulosx})

def crea_articulos(request): 

    if request.method == "POST":
        articulos_form = ArticulosForm(request.POST)
        if articulos_form.is_valid():
           data = articulos_form.cleaned_data
           articulo = Articulos(titulo=data["nombre_titulo"], subtitulo=data["nombre_subtitulo"])
           articulo.save()
           return render(request, 'core/index.html') #si sale todo bien nos manda al inicio

    articulos_form = ArticulosForm()
    return render (request, 'core/crear_articulos.html', {"form": articulos_form})

def edita_articulos(request): 
    return render (request, 'core/editar_articulos.html')

def elimina_articulos(request, id_articulo): 

    articulo = Articulos.objects.get(id=id_articulo)
    name = articulo.titulo
    articulo.delete()
    
    return render (request, 'core/eliminar_articulos.html', {"articulo_eliminado": name} )