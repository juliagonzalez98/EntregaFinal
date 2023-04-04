from django.urls import path, include
from core.views import inicio, muestra_articulos, crea_articulos, edita_articulos, elimina_articulos
urlpatterns = [
    path('', inicio, name="index"),
    path('mostrar-articulos/', muestra_articulos, name="mostrar"),
    path('crear-articulos/', crea_articulos, name="crear"),
    path ('editar-articulos/<id_articulo>/', edita_articulos, name="editar"),
    path('eliminar-articulos/<id_articulo>/', elimina_articulos, name="eliminar"),
  
    
]
