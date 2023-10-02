from django.shortcuts import render, redirect
from compra.models import Compra,Detalle_Compra
from compra.forms import CompraForm,CompraUpdateForm,Detalle_CompraForm,Detalle_CompraUpdateForm
from django.contrib import messages
import os

from django.contrib.auth.decorators import login_required
# Create your views here.
# Creación COMPRA crear,listar,modificar,eliminar


def compra_crear(request):
    titulo = "Compra"
    compra = Compra.objects.all()  # Obtén las compras desde la base de datos
    mensaje = f'¡Hecho! Se ha añadido con éxito la {titulo}.'
    mensajeerror = f'¡Oops! Hubo un error en el formulario de {titulo}. Por favor, revisa y corrige los campos resaltados en rojo.'
    if request.method == 'POST':
        form = CompraForm(request.POST)
        if form.is_valid():
            form.save()
            messages.success(request,mensaje)
            return redirect('compra')
        else:
            messages.error(request, mensajeerror)
    else:
        form = CompraForm()

    context = {
        "titulo": titulo,
        "form": form,
        "compra": compra  # Pasa las compras al contexto
    }

    return render(request, "compra/crear.html", context)


@login_required
def compra_listar(request):
    titulo="Compra"
    modulo="compras"
    compra = Compra.objects.all()
    context={
        "titulo":titulo,
        "modulo":modulo,
        "compra":compra,
    }
    return render(request,"compra/listar.html", context)

#@login_required
def compra_modificar(request,pk):
    titulo="Compra"
    compra= Compra.objects.get(id=pk)
    mensaje = f'¡Hecho! La {titulo} se ha modificado exitosamente.'
    if request.method== 'POST':
        form= CompraUpdateForm(request.POST, instance=compra)
        if form.is_valid():
            form.save()
            messages.success(request, mensaje)
            return redirect('compra')
        else:
            messages.error(request, 'Error Al Modificar La Compra')
    else:
        form= CompraUpdateForm(instance=compra)
    context={
        "titulo":titulo,
        "form":form
        }
    return render(request,"compra/modificar.html", context)

#@login_required
def compra_eliminar(request,pk):
    compra= Compra.objects.filter(id=pk)
    compra.update(
        estado="0"
    )
    return redirect('compra')

#Creación DETALLE COMPRA
#@login_required
def detalle_compra_crear(request):
    titulo = "Detalle Compra Crear"
    comprasn = Compra.objects.all()  # Obtén las compras desde la base de datos
    mensaje = f'¡Hecho! Se ha añadido con éxito el {titulo}.'
    mensajeerror = f'¡Oops! Hubo un error en el formulario de {titulo}. Por favor, revisa y corrige los campos resaltados en rojo.'
    if request.method == 'POST':
        form = Detalle_CompraForm(request.POST)
        if form.is_valid():
            form.save()
            messages.success(request, mensaje)
            return redirect('detalle_compra')
        else:
            messages.error(request,mensajeerror)
    else:
        form = Detalle_CompraForm()

    context = {
        "titulo": titulo,
        "comprasn": comprasn,
        "form": form  # Agrega el formulario al contexto
    }

    return render(request, "detalle_compra/crear.html", context)

#@login_required
def detalle_compra_listar(request):
    titulo="Detalle Compra"
    detalle_compras= Detalle_Compra.objects.all()
    context={
        "titulo":titulo,

        "detalle_compras":detalle_compras
    }
    return render(request,"detalle_compra/listar.html", context)

#@login_required
def detalle_compra_modificar(request,pk):
    titulo="Detalle_compra"
    detalle_compra = Detalle_Compra.objects.get(id=pk)
    mensaje = f'¡Hecho! El {titulo} se ha modificado exitosamente.'
    if request.method== 'POST':
        form= Detalle_CompraUpdateForm(request.POST, instance=detalle_compra)
        if form.is_valid():
            form.save()
            messages.success(request, mensaje)
            return redirect('detalle_compra')
        else:
            messages.error(request, 'Error Al Modificar El Detalle Compra')
    else:
        form= Detalle_CompraUpdateForm(instance=detalle_compra)
    context={
        "titulo":titulo,
        "form":form
        }
    return render(request,"detalle_compra/modificar.html", context)

