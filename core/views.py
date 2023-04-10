from django.shortcuts import render, get_object_or_404
from core.models import Articulos
from core.forms import ArticulosForm
from django.contrib.auth.decorators import login_required



# Create your views here.

def inicio(request):
    return render(request, 'core/index.html')
@login_required
def crea_articulos(request): 

    if request.method == "POST":
        articulos_form = ArticulosForm(request.POST, request.FILES)
        if articulos_form.is_valid():  
           data = articulos_form.cleaned_data
           titulo = data["titulo"]
           subtitulo = data["subtitulo"]
           cuerpo = data["cuerpo"]
           autor = data["autor"]
           imagen = data["imagen"]
           artic = Articulos(titulo=titulo, subtitulo=subtitulo, cuerpo=cuerpo, autor=autor, imagen=imagen)
           artic.save()
           id = articulos_form.id
           return render(request, 'core/mostrar_articulos.html', {'articulo.id':id}) #si sale todo bien nos manda a la lista de articulos
    else:
        articulos_form = ArticulosForm()
    return render (request, 'core/crear_articulos.html', {"form": articulos_form})

@login_required
def muestra_articulos(request): 

    articulosx = Articulos.objects.all()
    
    return render (request, 'core/mostrar_articulos.html', {"articulos": articulosx})

@login_required
def detalla_articulos(request, pk):
    articulo = get_object_or_404(Articulos, pk=pk)
    return render(request, 'core/detalla_articulos.html', {'articulo':articulo})

@login_required
def edita_articulos(request, id_articulo):
    articulo = Articulos.objects.get(id=id_articulo)

    if request.method == "POST":
        articulo_form = ArticulosForm(request.POST)
        if articulo_form.is_valid():
            data = articulo_form.cleaned_data
            articulo.titulo = data["nombre_titulo"]
            articulo.subtitulo = data["nombre_subtitulo"]
            articulo.save()
            return render(request, 'core/index.html')
    else: #metodo get
        articulo_form = ArticulosForm(initial={'nombre_titulo': Articulos.titulo, 'nombre_subtitulo': Articulos.subtitulo})
    return render (request, 'core/editar_articulos.html', {'form':articulo_form })

@login_required
def elimina_articulos(request, id_articulo): 

    articulo = Articulos.objects.get(id=id_articulo)
    name = articulo.titulo
    articulo.delete()
    
    return render (request, 'core/eliminar_articulos.html', {"articulo_eliminado": name} )

def acerca_de_mi(request):
    return render (request, 'core/about.html')



