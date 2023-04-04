from django.urls import path, include
from core.views import inicio, muestra_articulos, crea_articulos, edita_articulos, elimina_articulos, ArticulosList, ArticulosDetalle, ArticulosCreate, ArticulosUpdate, ArticulosDelete

urlpatterns = [
    path('', inicio, name="index"),
    path('mostrar-articulos/', muestra_articulos, name="mostrar"),
    path('crear-articulos/', crea_articulos, name="crear"),
    path ('editar-articulos/<int:id_articulo>/', edita_articulos, name="editar"),
    path('eliminar-articulos/<int:id_articulo>/', elimina_articulos, name="eliminar"),
    path('mostrar-view', ArticulosList.as_view(), name="mostrar_view"),
    path('detalle_view/<pk>/', ArticulosDetalle.as_view(), name="detalle_view"),
    path('crear_view', ArticulosCreate.as_view(), name="crear_view"),
    path('editar_view/<pk>/', ArticulosUpdate.as_view(), name="editar_view" ),
    path('eliminar_view/<pk>/', ArticulosDelete.as_view(),name="eliminar_view") 
    
]
