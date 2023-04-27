from django.urls import path
from venta.views import venta_crear, venta_listar, venta_modificar, venta_eliminar, detalle_venta_crear, detalle_venta_listar, detalle_venta_modificar

urlpatterns = [
    path('venta/',venta_listar, name = "ventas"),
    path('venta/crear/',venta_crear, name = "ventas-crear"),
    path('venta/modificar/<int:pk>/',venta_modificar, name = "ventas-modificar"),
    path('venta/eliminar/<int:pk>/',venta_eliminar, name = "ventas-eliminar"),

    path('detalle_venta/',detalle_venta_listar, name = "detalle_ventas"),
    path('detalle_venta/crear/',detalle_venta_crear, name = "detalle_venta-crear"),
    path('detalle_venta/modificar/<int:pk>/',detalle_venta_modificar, name = "detalle_venta-modificar")
    ]

