from django.shortcuts import render
from django.contrib.auth.forms import AuthenticationForm, UserCreationForm
from django.contrib.auth import login, logout, authenticate
from user.forms import UserRegisterForm, AvatarForm
from user.models import *
from django.contrib.auth.mixins import LoginRequiredMixin


# Create your views here.

def login_request(request):

    if request.method == "POST":

        form = AuthenticationForm(request, data = request.POST)

        if form.is_valid(): 
            usuario = form.cleaned_data.get('username')
            contrasenia = form.cleaned_data.get('password')

            user = authenticate(username= usuario, password=contrasenia)

            if user is not None:
                login(request, user)

                return render(request, "user/detalle_usuario.html", {"mensaje":f"Bienvenido {usuario}"})
            else:
                return render(request, "user/base.html", {"mensaje":"Datos incorrectos. Ingreselos nuevamente"})
           
        else:

            return render(request, "user/base.html", {"mensaje":"Formulario erroneo"})

    form = AuthenticationForm()

    return render(request, "user/login.html", {"form": form})

def register(request):
    if request.method == "POST":
        user_form = UserRegisterForm(request.POST)
        avatar_form = AvatarForm(request.POST, request.FILES)
        if user_form.is_valid() and avatar_form.is_valid():
            user = user_form.save(commit=False)
            user.save()

            avatar = avatar_form.save(commit=False)
            avatar.save()
            return render(request,"user/base.html" ,  {"mensaje":"Usuario Creado Exitosamente"})

    else:     
        user_form = UserRegisterForm()
        avatar_form = AvatarForm()   

    context = {'user_form': user_form, 'avatar_form': avatar_form}
    return render(request, 'user/registro.html', context)
    



