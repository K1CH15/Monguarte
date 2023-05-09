from django.urls import path

from productos.views import producto_listar, producto_crear, producto_modificar, producto_eliminar,tamaño_listar,tamaño_crear, tamaño_modificar, tamaño_eliminar,tipo_listar, tipo_crear, tipo_modificar, tipo_eliminar

urlpatterns = [
    path('producto/', producto_listar, name="productos" ),
    path('producto/crear/', producto_crear, name="productos-crear" ),
    path('producto/modificar/<int:pk>/', producto_modificar, name="productos-modificar" ),
    path('producto/eliminar/<int:pk>/', producto_eliminar, name="productos-eliminar" ),

    path('tamaño/', tamaño_listar, name="tamaños" ),
    path('tamaño/crear/', tamaño_crear, name="tamaños-crear" ),
    path('tamaño/modificar/<int:pk>/', tamaño_modificar, name="tamaños-modificar" ),
    path('tamaño/eliminar/<int:pk>/', tamaño_eliminar, name="tamaños-eliminar" ),

    path('tipo/', tipo_listar, name="tipos" ),
    path('tipo/crear/', tipo_crear, name="tipos-crear" ),
    path('tipo/modificar/<int:pk>/', tipo_modificar, name="tipos-modificar" ),
    path('tipo/eliminar/<int:pk>/', tipo_eliminar, name="tipos-eliminar" ),


]