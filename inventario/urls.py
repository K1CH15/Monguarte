from django.urls import path

from inventario.views import stock_crear,stock_eliminar,stock_listar,stock_modificar
from inventario.views import materia_prima_crear,materia_prima_eliminar,materia_prima_listar,materia_prima_modificar

urlpatterns = [
    path('stock/', stock_listar, name="stock"),
    path('compra/crear/', stock_crear, name="stock-crear" ),
    path('compra/modificar/<int:pk>/', stock_modificar, name="stock-modificar" ),
    path('compra/eliminar/<int:pk>/', stock_eliminar, name="stock-eliminar" ),

    path('materia prima/',materia_prima_listar, name="materia-prima"),
    path('materia prima/crear/', materia_prima_crear, name="materia-prima-crear" ),
    path('materia prima/modificar/<int:pk>/', materia_prima_modificar, name="materia-prima-modificar" ),
    path('materia prima/eliminar/<int:pk>/', materia_prima_eliminar, name="materia-prima-eliminar" ),
]