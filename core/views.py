from django.shortcuts import render, get_object_or_404
from core.models import Articulos
from core.forms import ArticulosForm
from django.contrib.auth.decorators import login_required
from django.http import HttpResponse
from user.models import Avatar


# Create your views here.

def inicio(request):
    try:
        avatar = Avatar.objects.get(user=request.user)
        context = {'imagen': avatar.imagen.url}
    except Avatar.DoesNotExist:
        context = {}
    return render(request, 'core/index.html', context)

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
           usuario = request.user
           articulo = Articulos(titulo=titulo, subtitulo=subtitulo, cuerpo=cuerpo, autor=autor, imagen=imagen, usuario=usuario)
           articulo.save()
           id = articulo.id
           return render(request, 'core/mostrar_postcrear.html', {"mensaje": "Recomendacion agregada correctamente",'articulo':articulo}) #si sale todo bien nos manda a la lista de articulos
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
        articulo_form = ArticulosForm(request.POST, request.FILES)
        if articulo_form.is_valid():
            data = articulo_form.cleaned_data
            articulo.titulo = data["titulo"]
            articulo.subtitulo = data["subtitulo"]
            articulo.cuerpo= data["cuerpo"]
            articulo.autor = data["autor"]
            if 'imagen' in request.FILES:
             articulo.imagen = data["imagen"]

#verificamos si el usuario que intenta editar es el que creó el artículo
            if articulo.usuario == request.user:
               articulo.save()
               return render(request, 'core/mostrar_posteditar.html', {'articulo':articulo})
            else:
                return render(request, 'core/autorización.html')
        
    else: #metodo get
        if articulo.usuario == request.user or request.user.is_staff:
           articulo_form=ArticulosForm(initial={'titulo':articulo.titulo, 'subtitulo':articulo.subtitulo, 'cuerpo':articulo.cuerpo,'autor':articulo.autor, 'imagen':articulo.imagen})
           return render (request, 'core/editar_articulos.html', {'articulo_form':articulo_form})
        else:
             return render(request, 'core/autorización.html')

@login_required
def elimina_articulos(request, id_articulo): 

    articulo = Articulos.objects.get(id=id_articulo)
    name = articulo.titulo

    if articulo.usuario == request.user:         
      articulo.delete()
      return render (request, 'core/eliminar_articulos.html', {"articulo_eliminado": name} )
    else:
        return render(request, 'core/autorización.html')
       

def acerca_de_mi(request):
    return render (request, 'core/about.html')



