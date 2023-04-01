from django.shortcuts import render
from core.models import Articulos

# Create your views here.

def inicio(request):
    return render(request, 'core/index.html')

def muestra_articulos(request): #boton

    articulosx = Articulos.objects.all()
    
    return render (request, 'core/mostrar_articulos.html', {"articulos": articulosx})

def crea_articulos(request): #boton
    return render (request, 'core/crear_articulos.html')

def edita_articulos(request): #sin boton
    return render (request, 'core/editar_articulos.html')

def elimina_articulos(request): #sin boton 
    return render (request, 'core/eliminar_articulos.html')