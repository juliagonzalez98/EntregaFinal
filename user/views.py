from django.shortcuts import render,redirect
from django.contrib.auth.forms import AuthenticationForm, UserCreationForm, PasswordChangeForm
from django.contrib.auth import login, logout, authenticate
from user.forms import UserRegisterForm, AvatarForm, UserEditForm
from user.models import *
from core.models import Articulos
from user.views import *
from django.contrib.auth.mixins import LoginRequiredMixin
from django.contrib.auth.decorators import login_required
from django.views.generic import ListView
from django.contrib.auth.models import User



# Create your views here.

def login_request(request):

    if request.method == "POST":

        form = AuthenticationForm(request, data = request.POST)

        if form.is_valid(): 
            usuario = form.cleaned_data.get('username')
            contrasenia = form.cleaned_data.get('password')

            user = authenticate(username= usuario, password=contrasenia)
            articulosx = Articulos.objects.all()

            if user is not None:
                login(request, user)

                return render(request, "core/mostrar_articulos.html", {"articulos": articulosx,"mensaje":f"Bienvenido {usuario}"})
            else:
                return render(request, "user/base.html", {"mensaje":"Datos incorrectos. Ingreselos nuevamente"})
           
        else:

            return render(request, "user/base.html", {"mensaje":"Formulario erroneo"})

    form = AuthenticationForm()

    return render(request, "user/login.html", {"form": form})

def register(request):
    if request.method == "POST":
        form = UserRegisterForm(request.POST)
        if form.is_valid():
                username = form.cleaned_data['username']
                form.save()
                return render(request,"user/base.html" ,  {"mensaje":"Usuario Creado Exitosamente"})
    else:     
        form = UserRegisterForm()     
    return render(request,"user/registro.html" , {"form":form})

def  agrega_avatar(request):
    if request.method == "POST":
        miFormulario = AvatarForm(request.POST, request.FILES)

        if miFormulario.is_valid():
            u = User.objects.get(username=request.user)
            avatar = Avatar(user = u, imagen=miFormulario.cleaned_data['imagen'])
            avatar.save()
            return render (request,"user/agrega_avatar.html", {"mensaje":"Usuario Creado Exitosamente"})
    else:
        miFormulario = AvatarForm()
    return render(request, "user/agregar_avatar.html", {"miFormulario": miFormulario })

@login_required
def editarPerfil(request):
    usuario = request.user

    if request.method == 'POST':
        miFormulario = UserEditForm(request.POST, request.FILES, instance=usuario)
        if miFormulario.is_valid():
            usuario = miFormulario.save(commit=False)
            usuario.set_password(miFormulario.cleaned_data["password1"])
            usuario.save()
            return(request, "user/detalle_usuario.html", {"mensaje":"Cambios guardados"})
    else:
        miFormulario = UserEditForm(instance=usuario)

    return render(request, "user/editar-perfil.html", {"miFormulario": miFormulario, "usuario": usuario})

@login_required
def detallaUser(request):
   usuario = request.user
   return render(request, "user/detalle_usuario.html", {'usuario': usuario})