from django.urls import path

from inventario.views import stock_producto_crear,stock_producto_eliminar,stock_producto_listar,stock_producto_modificar
from inventario.views import materia_prima_crear,materia_prima_eliminar,materia_prima_listar,materia_prima_modificar
from inventario.views import stock_materia_prima_modificar,stock_materia_prima_crear,stock_materia_prima_eliminar,stock_materia_prima_listar
urlpatterns = [
    path('stock producto/', stock_producto_listar, name="stock-productos"),
    path('stock producto/crear/', stock_producto_crear, name="stock-producto-crear" ),
    path('stock producto/modificar/<int:pk>/', stock_producto_modificar, name="stock-producto-modificar" ),
    path('stock producto/eliminar/<int:pk>/', stock_producto_eliminar, name="stock-producto-eliminar" ),

    path('materia prima/',materia_prima_listar, name="materias-primas"),
    path('materia prima/crear/', materia_prima_crear, name="materia-prima-crear" ),
    path('materia prima/modificar/<int:pk>/', materia_prima_modificar, name="materia-prima-modificar" ),
    path('materia prima/eliminar/<int:pk>/', materia_prima_eliminar, name="materia-prima-eliminar" ),

    path('stock materia prima/',stock_materia_prima_listar, name="stock-materias-primas"),
    path('stock materia prima/crear/', stock_materia_prima_crear, name="stock-materia-prima-crear" ),
    path('stock materia prima/modificar/<int:pk>/',stock_materia_prima_modificar, name="stock-materia-prima-modificar" ),
    path('stock materia prima/eliminar/<int:pk>/', stock_materia_prima_eliminar, name="stock-materia-prima-eliminar" ),
]