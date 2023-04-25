from django.urls import path

from compra.views import compra_listar, compra_crear, compra_modificar, compra_eliminar, detalle_compra_listar, detalle_compra_crear, detalle_compra_modificar

urlpatterns = [
    path('compra/', compra_listar, name="compra"),
    path('compra/crear/', compra_crear, name="compra-crear" ),
    path('compra/modificar/<int:pk>/', compra_modificar, name="compra-modificar" ),
    path('compra/eliminar/<int:pk>/', compra_eliminar, name="compra-eliminar" ),

    path('detalle_compra/', detalle_compra_listar, name="detalle_compra" ),
    path('detalle_compra/crear/', detalle_compra_crear, name="detalle_compra-crear" ),
    path('detalle_compra/modificar/<int:pk>/', detalle_compra_modificar, name="detalle_compra-modificar" ),
]