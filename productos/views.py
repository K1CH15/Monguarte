from django.contrib import messages
from django.shortcuts import render, redirect
from django.contrib.auth.decorators import login_required
from productos.forms import ProductoForm, ProductoUpdateForm
from productos.models import Producto


# Create your views here.
@login_required
def producto_crear(request):
    titulo = "Producto"
    mensaje = f'¡Hecho! Se ha añadido con éxito el {titulo}.'
    mensajeerror = f'¡Oops! Hubo un error en el formulario de {titulo}. Por favor, revisa y corrige los campos resaltados en rojo.'
    if request.method == 'POST':
        form = ProductoForm(request.POST)
        if form.is_valid():
            form.save()
            messages.success(request, mensaje)

            return redirect('productosl')
        else:
            messages.error(request,mensajeerror)
    else:
        form = ProductoForm()
    context = {
        "titulo": titulo,
        "form": form
    }
    return render(request, "productos/crear.html", context)

@login_required
def producto_listar(request):
    titulo = "Producto"
    modulo = "productos"
    productosn = Producto.objects.all()
    context = {
        "titulo": titulo,
        "modulo": modulo,
        "productos": productosn
    }
    return render(request, "productos/listar.html", context)

@login_required
def producto_modificar(request, pk):
    titulo = "Producto"
    producto = Producto.objects.get(id=pk)
    mensaje = f'¡Hecho! El {titulo} se ha modificado exitosamente.'
    if request.method == 'POST':
        form = ProductoUpdateForm(request.POST, instance=producto)
        if form.is_valid():
            form.save()
            messages.success(request, mensaje)
            return redirect('productosl')
    else:
        form = ProductoUpdateForm(instance=producto)
    context = {
        "titulo": titulo,
        "form": form
    }
    return render(request, "productos/modificar.html", context)

@login_required
def producto_eliminar(request, pk):
    mensaje = f'¡Hecho! El P se ha modificado exitosamente.'
    producto = Producto.objects.filter(id=pk)
    producto.update(
        estado="0",
    )
    messages.info(request, '¡Hecho! El Producto se ha eliminado exitosamente.')

    return redirect('productosl')
