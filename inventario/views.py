from django.contrib import messages
from django.shortcuts import render, redirect
from django.contrib.auth.decorators import login_required
from inventario.forms import FabricacionForm, FabricacionUptadeForm, Fabricacion
from inventario.forms import Materia_PrimaForm, Materia_PrimaUptadeForm, Materia_Prima
from inventario.models import Materia_Prima
from productos.forms import ProductoForm
from productos.models import Producto


# Create your views here.

# CRUD Materia Prima

@login_required
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


@login_required
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


@login_required
def materia_prima_eliminar(request, pk):
    materia_prima = Materia_Prima.objects.filter(id=pk)
    materia_prima.update(
        estado="0"
    )
    return redirect('materias-primas')


# CRUD Stock_Materia_Prima

@login_required
def fabricacion_crear(request):
    titulo = "Fabricación"
    mensaje = f'¡Hecho! Se ha añadido con éxito la {titulo}.'
    mensajeerror = f'¡Oops! Hubo un error en el formulario de {titulo}. Por favor, revisa y corrige los campos resaltados en rojo.'

    if request.method == 'POST':
        form = FabricacionForm(request.POST)
        if form.is_valid():
            cantidad_materia = form.cleaned_data['cantidad_materia']
            materia_prima_stock = form.cleaned_data['materia_prima'].stock

            if cantidad_materia > materia_prima_stock:
                messages.error(request,
                               f'No hay suficiente stock de materia prima disponible. Cantidad en stock: {materia_prima_stock}')
            else:
                fabricacion = form.save()  # Guardar la fabricación

                # Calcular el costo de fabricación
                costo_fabricacion = fabricacion.calcular_costo_fabricacion()

                # Asignar el costo de fabricación al producto
                fabricacion.producto.calcular_costo_fabricacion = costo_fabricacion
                fabricacion.producto.save()

                messages.success(request, mensaje)
                return redirect('fabricaciones')
                form.save()
                messages.success(request, mensaje)
                return redirect('fabricaciones')
        else:
            messages.error(request, mensajeerror)

    else:

        form = FabricacionForm()
        materia_activa = Materia_Prima.objects.filter(estado='1')
        form.fields['materia_prima'].queryset = materia_activa
        producto_activo = Materia_Prima.objects.filter(estado='1')
        form.fields['producto'].queryset = producto_activo

    context = {"titulo": titulo, "form": form}

    return render(request, "fabricacion/crear.html", context)


@login_required
def fabricacion_listar(request):
    titulo = "Fabricacion"
    modulo = "inventarios"
    fabricacion = Fabricacion.objects.all()
    context = {
        "titulo": titulo,
        "modulo": modulo,
        "fabricas": fabricacion,
    }
    return render(request, "fabricacion/listar.html", context)


@login_required
def fabricacion_modificar(request, pk):
    titulo = "Fabricacion"
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


@login_required
def fabricacion_eliminar(request, pk):
    fabricacion = Fabricacion.objects.filter(id=pk)
    fabricacion.update(
        estado="0"
    )
    return redirect('fabricaciones')

# def listar_stock(request):
#     titulo = "Stock"
#     modulo = "inventarios"
#     stock = Stock.objects.all()
#     context = {
#         "titulo": titulo,
#         "modulo": modulo,
#         "stock": stock,
#     }
#     return render(request, 'stock/listar_stock.html', context)
#
# def agregar_stock(request):
#     if request.method == 'POST':
#         form = StockForm(request.POST)
#         if form.is_valid():
#             form.save()
#             return redirect('stock:listar_stock')
#
#     else:
#         form = StockForm()
#
#     return render(request, 'stock/listar_stock.html', {'form': form})
