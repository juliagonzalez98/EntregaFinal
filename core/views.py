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
           articulo = Articulos(titulo=data["nombre_titulo"], subtitulo=data["nombre_subtitulo"], cuerpo=data["cuerpo"], autor=data["autor"],fecha=data["fecha"], imagen=data["imangen"] )
           articulo.save()
           return render(request, 'core/index.html') #si sale todo bien nos manda a inicio

    articulos_form = ArticulosForm()
    return render (request, 'core/crear_articulos.html', {"form": articulos_form})

def edita_articulos(request, id_articulo):
    articulo = Articulos.objects.get(id=id_articulo)

    if request.method == "POST":
        articulo_form = ArticulosForm(request.POST)
        print(articulo_form)
        if articulo_form.is_valid():
            data = articulo_form.cleaned_data
            articulo.titulo = data["nombre_titulo"]
            articulo.subtitulo = data["nombre_subtitulo"]
            articulo.save()
            return render(request, 'core/index.html')
    else: #metodo get
        articulo_form = ArticulosForm(initial={'nombre_titulo': Articulos.titulo, 'nombre_subtitulo': Articulos.subtitulo})
    return render (request, 'core/editar_articulos.html', {'form':articulo_form })

def elimina_articulos(request, id_articulo): 

    articulo = Articulos.objects.get(id=id_articulo)
    name = articulo.titulo
    articulo.delete()
    
    return render (request, 'core/eliminar_articulos.html', {"articulo_eliminado": name} )

def acerca_de_mi(request):
    return render (request, 'core/about.html')



