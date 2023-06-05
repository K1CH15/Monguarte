from django.urls import path
from usuario.views import persona_crear,persona_listar,persona_modificar,persona_eliminar
from usuario.views import contabilidad_crear,contabilidad_listar,contabilidad_modificar,contabilidad_eliminar
from usuario.views import aporte_crear,aporte_listar,aporte_modificar,aporte_eliminar
from usuario.views import ips_crear,ips_listar,ips_modificar,ips_eliminar
from usuario.views import nomina_crear,nomina_listar,nomina_modificar,nomina_eliminar
from usuario.views import trabajador_crear,trabajador_listar,trabajador_modificar


urlpatterns = [
    path('persona/', persona_listar, name="personas"),
    path('persona/crear/', persona_crear, name="personas-crear" ),
    path('persona/modificar/<int:pk>/', persona_modificar, name="personas-modificar" ),
    path('persona/eliminar/<int:pk>/', persona_eliminar, name="personas-eliminar" ),

    path('contabilidad/', contabilidad_listar , name="contabilidades"),
    path('contabilidad/crear/', contabilidad_crear , name="contabilidades-crear" ),
    path('contabilidad/modificar/<int:pk>/', contabilidad_modificar , name="contabilidades-modificar" ),
    path('contabilidad/eliminar/<int:pk>/', contabilidad_eliminar , name="contabilidades-eliminar" ),

    path('aporte/', aporte_listar , name="aportes"),
    path('aporte/crear/', aporte_crear , name="aportes-crear" ),
    path('aporte/modificar/<int:pk>/', aporte_modificar , name="aportes-modificar" ),
    path('aporte/eliminar/<int:pk>/', aporte_eliminar , name="aportes-eliminar" ),

    path('ips/',ips_listar , name="ipss"),
    path('ips/crear/',ips_crear , name="ipss-crear" ),
    path('ips/modificar/<int:pk>/', ips_modificar , name="ipss-modificar" ),
    path('ips/eliminar/<int:pk>/',ips_eliminar , name="ipss-eliminar" ),

    path('nomina/',nomina_listar , name="nominas"),
    path('nomina/crear/',nomina_crear , name="nominas-crear" ),
    path('nomina/modificar/<int:pk>/',nomina_modificar , name="nominas-modificar" ),
    path('nomina/eliminar/<int:pk>/',nomina_eliminar , name="nominas-eliminar" ),

    path('trabajador/',trabajador_listar , name="trabajadores"),
    path('trabajador/crear/',trabajador_crear , name="trabajadores-crear" ),
    path('trabajador/modificar/<int:pk>/', trabajador_modificar, name="trabajadores-modificar"),


]
