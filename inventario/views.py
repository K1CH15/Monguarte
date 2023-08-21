from django.contrib import messages
from django.shortcuts import render, redirect

from inventario.forms import FabricacionForm, FabricacionUptadeForm, Fabricacion
from inventario.forms import Materia_PrimaForm, Materia_PrimaUptadeForm, Materia_Prima



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
            cantidad_materia = form.cleaned_data['cantidad_materia']
            materia_prima_stock = form.cleaned_data['materia_prima'].stock

            if cantidad_materia > materia_prima_stock:
                messages.error(request, f'No hay suficiente stock de materia prima disponible. Cantidad en stock: {materia_prima_stock}')
            else:
                form.save()
                messages.success(request, mensaje)
                return redirect('fabricaciones')
        else:
            messages.error(request, mensajeerror)

    else:
        form = FabricacionForm()

    context = {"titulo": titulo, "form": form}
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

#
