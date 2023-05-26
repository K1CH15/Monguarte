from django.shortcuts import render,redirect
from django.contrib.auth.decorators import login_required
from django.contrib.auth import logout
from compra.models import Compra,Detalle_Compra
from venta.models import Venta,Detalle_Venta
from inventario.models import Materia_Prima,Stock_Materia_Prima,Detalle_Producto,Stock_Producto
from productos.models import Tipo,Tamaño,Producto
from usuario.models import Persona,Trabajador,Aporte,Contabilidad,Ips,Nomina
#@login_required
def principal(request):
    titulo="Bienvenido"
    compras= Compra.objects.all().count
    detalle_compras=Detalle_Compra.objects.all().count()
    ventas=Venta.objects.all().count()
    detalle_ventas=Detalle_Venta.objects.all().count()
    materias_primas=Materia_Prima.objects.all().count()
    stock_materias_primas=Stock_Materia_Prima.objects.all().count()
    detalle_productos=Detalle_Producto.objects.all().count()
    stock_productos=Stock_Producto.objects.all().count()
    tipos=Tipo.objects.all().count()
    tamaños=Tamaño.objects.all().count()
    productos=Producto.objects.all().count()
    personas=Persona.objects.all().count()
    trabajadores=Trabajador.objects.all().count()
    aportes=Aporte.objects.all().count()
    contabilidades=Contabilidad.objects.all().count()
    ipss=Ips.objects.all().count()
    nominas=Nomina.objects.all().count()

    context={
        "titulo":titulo,
        "compras":compras,
        "detalle_compras":detalle_compras,
        "ventas":ventas,
        "detalle_ventas":detalle_ventas,
        "materias_primas":materias_primas,
        "stock_materias_primas":stock_materias_primas,
        "detalle_productos":detalle_productos,
        "stock_productos":stock_productos,
        "tipos":tipos,
        "tamaños":tamaños,
        "productos":productos,
        "personas":personas,
        "trabajadores":trabajadores,
        "aportes":aportes,
        "contabilidades":contabilidades,
        "ipss":ipss,
        "nominas":nominas
    }
    return render(request,"index.html",context)

def logout_user(request):
    logout(request)
    return redirect('inicio')
