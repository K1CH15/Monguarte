from django.urls import path
from inventario.views import fabricacion_listar, fabricacion_crear, fabricacion_modificar, fabricacion_eliminar
from inventario.views import materia_prima_crear, materia_prima_eliminar, materia_prima_listar, materia_prima_modificar

urlpatterns = [

    path('materia prima/', materia_prima_listar, name="materias-primas"),
    path('materia prima/crear/', materia_prima_crear, name="materias-primas-crear"),
    path('materia prima/modificar/<int:pk>/', materia_prima_modificar, name="materias-primas-modificar"),
    path('materia prima/eliminar/<int:pk>/', materia_prima_eliminar, name="materias-primas-eliminar"),

    path('fabricacion/', fabricacion_listar, name="fabricaciones"),
    path('fabricacion/crear/', fabricacion_crear, name="fabricaciones-crear"),
    path('fabricacion/modificar/<int:pk>/', fabricacion_modificar, name="fabricaciones-modificar"),
    path('fabricacion/eliminar/<int:pk>/', fabricacion_eliminar, name="fabricaciones-eliminar"),
    # path('stock/', listar_stock, name='stock'),
    # path('stock/agregar/', agregar_stock, name='agregar_stock'),

]
