from django.urls import path, include
from django.contrib.auth.decorators import login_required
from core.views import inicio, muestra_articulos, crea_articulos, edita_articulos, elimina_articulos, acerca_de_mi, detalla_articulos
urlpatterns = [
    path('', inicio, name="index"),
    path('mostrar-articulos/', login_required(muestra_articulos), name="mostrar"),
    path('detalle/<int:pk>/', login_required(detalla_articulos), name="detalle"),
    path('crear-articulos/', login_required(crea_articulos), name="crear"),
    path('editar-articulos/<id_articulo>/', login_required(edita_articulos), name="editar"),
    path('eliminar-articulos/<id_articulo>/', login_required(elimina_articulos), name="eliminar"),
    path('AboutMe', acerca_de_mi, name="AboutMe"),
    path('user/', include('user.urls')),
  
    
]
