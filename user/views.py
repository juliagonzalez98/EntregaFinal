from django.shortcuts import render
from django.contrib.auth.forms import AuthenticationForm
from django.contrib.auth import login, logout, authenticate

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

                return render(request, "core/index.html", {"mensaje":f"Bienvenido {usuario}"})
            else:
                return render(request, "core/index.html", {"mensaje":"Datos incorrectos. Ingreselos nuevamente"})
           
        else:

            return render(request, "core/index.html", {"mensaje":"Formulario erroneo"})

    form = AuthenticationForm()

    return render(request, "user/login.html", {"form": form})

