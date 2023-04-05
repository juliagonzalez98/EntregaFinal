from django.shortcuts import render
from django.contrib.auth.forms import AuthenticationForm, UserCreationForm
from django.contrib.auth import login, logout, authenticate
from user.forms import UserRegisterForm

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

                return render(request, "user/detalle.html", {"mensaje":f"Bienvenido {usuario}"})
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

