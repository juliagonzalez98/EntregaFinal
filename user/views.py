from django.shortcuts import render,redirect
from django.contrib.auth.forms import AuthenticationForm, UserCreationForm, PasswordChangeForm
from django.contrib.auth import login, logout, authenticate
from user.forms import UserRegisterForm, UserEditForm, AvatarForm
from user.models import *
from core.models import Articulos
from user.views import *
from django.contrib.auth.mixins import LoginRequiredMixin
from django.contrib.auth.decorators import login_required
from django.views.generic import ListView
from django.contrib.auth.models import User
from django.core.cache import cache
from user.utilities.user_profile import clean_avatar_record_without_user
from django.urls import reverse


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


@login_required
def editarPerfil(request):
    usuario = request.user

    if request.method == 'POST':
        miFormulario = UserEditForm(request.POST, request.FILES, instance=usuario)
        if miFormulario.is_valid():
            informacion = miFormulario.cleaned_data
            usuario.username = informacion['username']
            usuario.email = informacion['email']
            usuario.set_password(informacion['password1'])
            usuario.name = informacion['name']
            usuario.save()
            cache.delete('user_{}'.format(request.user.pk))

            return redirect('perfil', mensaje="Cambios guardados")
    else:
        miFormulario = UserEditForm(instance=usuario)

    return render(request, "user/editar-perfil.html", {"miFormulario": miFormulario, "usuario": usuario})


@login_required
def detallaUser(request):
   
   usuario = request.user
   return render(request, "user/detalle_usuario.html", {'usuario': usuario})

@login_required
def AgregaAvatar(request):
    mensaje = ""
    if request.method == "POST":
        form = AvatarForm(request.POST, request.FILES)
        if form.is_valid():
            avatar = form.save()
            avatar.user = request.user
            avatar.save()
            clean_avatar_record_without_user()
            return redirect(reverse('perfil'))
        else:
            mensaje = "Error al agregar el avatar"
    
    form = AvatarForm()
    return render(request, "user/agregar_avatar.html", {"form": form, "msj": mensaje})