from django.contrib import messages
from django.shortcuts import render, redirect

from inventario.forms import FabricacionForm, FabricacionUptadeForm, Fabricacion
from inventario.forms import Materia_PrimaForm, Materia_PrimaUptadeForm, Materia_Prima
from inventario.forms import Unidad_MedidaForm, Unidad_MedidaUptadeForm, Unidad_Medida


# Create your views here.

# CRUD Materia Prima

# @login_required
def materia_prima_crear(request):
    titulo = "materia prima"
    mensaje = f'¡Hecho! Se ha añadido con éxito la {titulo}.'
    mensajeerror = f'¡Oops! Hubo un error en el formulario de {titulo}. Por favor, revisa y corrige los campos resaltados en rojo.'
    if request.method == 'POST':
        form = Materia_PrimaForm(request.POST)
        if form.is_valid():
            form.save()
            messages.success(request, mensaje)
            return redirect('materias-primas')
        else:
            messages.error(request, mensajeerror)

    else:
        form = Materia_PrimaForm()
    context = {
        "titulo": titulo,
        "form": form
    }
    return render(request, "materia prima/crear.html", context)


# @login_required
def materia_prima_listar(request):
    titulo = "Materia Prima"
    modulo = "inventarios"
    m = Materia_Prima.objects.all()
    context = {
        "titulo": titulo,
        "modulo": modulo,
        "materias": m,
    }
    return render(request, "materia prima/listar.html", context)


# @login_required
def materia_prima_modificar(request, pk):
    titulo = "materia prima"
    mensaje = f'¡Hecho! La {titulo} se ha modificado exitosamente.'
    materia_prima = Materia_Prima.objects.get(id=pk)
    if request.method == 'POST':
        form = Materia_PrimaUptadeForm(request.POST, instance=materia_prima)
        if form.is_valid():
            form.save()
            messages.success(request, mensaje)
            return redirect('materias-primas')
    else:
        form = Materia_PrimaUptadeForm(instance=materia_prima)
    context = {
        "titulo": titulo,
        "form": form
    }
    return render(request, "materia prima/modificar.html", context)


# @login_required
def materia_prima_eliminar(request, pk):
    materia_prima = Materia_Prima.objects.filter(id=pk)
    materia_prima.update(
        estado="0"
    )
    return redirect('materias-primas')


# CRUD Stock_Materia_Prima

# @login_required
def fabricacion_crear(request):
    titulo = "Fabricación"
    mensaje = f'¡Hecho! Se ha añadido con éxito la {titulo}.'
    mensajeerror = f'¡Oops! Hubo un error en el formulario de {titulo}. Por favor, revisa y corrige los campos resaltados en rojo.'
    if request.method == 'POST':
        form = FabricacionForm(request.POST)
        if form.is_valid():
            form.save()
            messages.success(request, mensaje)
            return redirect('fabricaciones')
        else:
            messages.error(request, mensajeerror)
    else:
        form = FabricacionForm()
    context = {
        "titulo": titulo,
        "form": form
    }
    return render(request, "fabricacion/crear.html", context)


# @login_required
def fabricacion_listar(request):
    titulo = "Fabricación"
    modulo = "inventarios"
    fabricacion = Fabricacion.objects.all()
    context = {
        "titulo": titulo,
        "modulo": modulo,
        "fabricas": fabricacion,
    }
    return render(request, "fabricacion/listar.html", context)


# @login_required
def fabricacion_modificar(request, pk):
    titulo = "Fabricación"
    mensaje = f'¡Hecho! La {titulo} se ha modificado exitosamente.'
    fabricacion = Fabricacion.objects.get(id=pk)
    if request.method == 'POST':
        form = FabricacionUptadeForm(request.POST, instance=fabricacion)
        if form.is_valid():
            form.save()
            messages.success(request, mensaje)
            return redirect('fabricaciones')
    else:
        form = FabricacionUptadeForm(instance=fabricacion)
    context = {
        "titulo": titulo,
        "form": form
    }
    return render(request, "fabricacion/modificar.html", context)


# @login_required
def fabricacion_eliminar(request, pk):
    fabricacion = Fabricacion.objects.filter(id=pk)
    fabricacion.update(
        estado="0"
    )
    return redirect('fabricaciones')


# CRUD Stock_Producto

# @login_required
def unidad_medida_crear(request):
    titulo = "Unidad de Medida"
    mensaje = f'¡Hecho! Se ha añadido con éxito la {titulo}.'
    mensajeerror = f'¡Oops! Hubo un error en el formulario de {titulo}. Por favor, revisa y corrige los campos resaltados en rojo.'
    if request.method == 'POST':
        form = Unidad_MedidaForm(request.POST)
        if form.is_valid():
            form.save()
            messages.success(request, mensaje)
            return redirect('unidades-medida')
        else:
            messages.error(request, mensajeerror)
    else:
        form = Unidad_MedidaForm()
    context = {
        "titulo": titulo,
        "form": form
    }
    return render(request, "unidad de medida/crear.html", context)


# @login_required
def unidad_medida_listar(request):
    titulo = "Unidad Medida"
    modulo = "inventarios"
    unidade_medida = Unidad_Medida.objects.all()
    context = {
        "titulo": titulo,
        "modulo": modulo,
        "unidades": unidade_medida,
    }
    return render(request, "unidad de medida/listar.html", context)


# @login_required
def unidad_medida_modificar(request, pk):
    titulo = "Unidad Medida"
    mensaje = f'¡Hecho! La {titulo} se ha modificado exitosamente.'
    unidad_medida = Unidad_Medida.objects.get(id=pk)
    if request.method == 'POST':
        form = Unidad_MedidaUptadeForm(request.POST, instance=unidad_medida)
        if form.is_valid():
            form.save()
            messages.success(request,mensaje)
            return redirect('unidades-medida')
    else:
        form = Unidad_MedidaUptadeForm(instance=unidad_medida)
    context = {
        "titulo": titulo,
        "form": form
    }
    return render(request, "unidad de medida/modificar.html", context)


def unidad_medida_eliminar(request, pk):
    unidad = Unidad_Medida.objects.filter(id=pk)
    unidad.delete()
    return redirect('unidades-medida')

# #@login_required
# def stock_producto_eliminar(request,pk):
#     stock_producto=Stock_Producto.objects.filter(id=pk)
#     stock_producto.update(
#         estado="0"
#     )
#     return redirect('stock-productos')
#
# #CRUD detalle_Producto
#
# #@login_required
# def detalle_producto_crear(request):
#     titulo="detalle producto"
#     if request.method == 'POST':
#         form=Detalle_ProductoForm(request.POST)
#         if form.is_valid():
#             form.save()
#             messages.success(request,'falta')
#             return redirect('detalle-productos')
#         else:
#             messages.error(request,'¡Oops! Parece que ha ocurrido un error en el formulario. Te pedimos que revises los campos resaltados y realices las correcciones necesarias.')
#     else:
#         form=Detalle_ProductoForm()
#     context={
#         "titulo":titulo,
#         "form":form
#     }
#     return render(request,"detalle_producto/crear.html",context)
#
#
# #@login_required
# def detalle_producto_listar(request):
#     titulo="detalle producto"
#     modulo="inventario"
#     detalle_producto=Detalle_Producto.objects.all()
#     context={
#         "titulo":titulo,
#         "modulo":modulo,
#         "detallesP":detalle_producto,
#     }
#     return render(request,"detalle_producto/listar.html",context)
#
#
# #@login_required
# def detalle_producto_modificar(request,pk):
#     titulo="detalle producto"
#     detalle_producto=Detalle_Producto.objects.get(id=pk)
#     if request.method=='POST':
#         form=Detalle_ProductoUptadeForm(request.POST,instance=detalle_producto)
#         if form.is_valid():
#             form.save()
#             return redirect('detalle-productos')
#     else:
#         form=Stock_Materia_Prima(instance=detalle_producto)
#     context={
#         "titulo":titulo,
#         "form":form
#     }
#     return render (request,"detalle_producto/modificar.html",context)
#
