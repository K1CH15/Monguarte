from django.shortcuts import render, redirect
from venta.models import Venta, Detalle_Venta
from venta.forms import Detalle_VentaForm,Detalle_VentaUpdateForm,VentaForm,VentaUpdateForm
from django.contrib import messages
from django.contrib.auth.decorators import login_required

# Create your views here.
#VIEWS VENTA

@login_required
def venta_crear(request):
    titulo="Venta"
    mensaje = f'¡Hecho! Se ha añadido con éxito la {titulo}.'
    mensajeerror = f'¡Oops! Hubo un error en el formulario de {titulo}. Por favor, revisa y corrige los campos resaltados en rojo.'
    if request.method=='POST':
        form=VentaForm(request.POST)
        if form.is_valid():
            form.save()
            messages.success(request, mensaje)
            return redirect('ventas')
        else:
            messages.error(request, mensajeerror)
    else:
        form=VentaForm()
    context={"titulo":titulo,"form":form}
    return render(request,"venta/crear.html", context)


@login_required
def venta_listar(request):
    titulo="Venta"
    modulo="ventas"
    venta=Venta.objects.all()
    context={"titulo":titulo,"venta":venta,"modulo": modulo}
    return render(request,"venta/listar.html", context)


@login_required
def venta_modificar(request,pk):
    titulo="Venta"
    mensaje = f'¡Hecho! La {titulo} se ha modificado exitosamente.'
    venta=Venta.objects.get(id=pk)

    if request.method=='POST':
        form=VentaUpdateForm(request.POST, instance=venta)
        if form.is_valid():
            form.save()
            messages.success(request, mensaje)
            return redirect('ventas')
    else:
        form=VentaUpdateForm(instance=venta)
    context={"titulo":titulo,"form":form}
    return render(request,"venta/modificar.html", context)


@login_required
def venta_eliminar(request,pk):
    venta=Venta.objects.filter(id=pk)
    venta.update(estado="0")
    return redirect('ventas')

#VIEWS DETALLE_VENTA

@login_required
def detalle_venta_crear(request):
    titulo = "Detalle Venta"
    mensaje = f'¡Hecho! Se ha añadido con éxito el {titulo}.'
    mensajeerror = f'¡Oops! Hubo un error en el formulario de {titulo}. Por favor, revisa y corrige los campos resaltados en rojo.'

    if request.method == 'POST':
        form = Detalle_VentaForm(request.POST)
        if form.is_valid():
            cantidad_total = form.cleaned_data['cantidad_total']
            producto_stock = form.cleaned_data['producto'].stock

            if cantidad_total > producto_stock:
                messages.error(request, f'No hay suficiente stock del producto disponible. Cantidad en stock: {producto_stock}')
            else:
                form.save()
                messages.success(request, mensaje)
                return redirect('detalle_ventas')
        else:
            for field, errors in form.errors.items():
                for error in errors:
                    messages.error(request, f'{field}: {error}')
            messages.error(request, mensajeerror)

    else:
        form = Detalle_VentaForm()

    context = {"titulo": titulo, "form": form}
    return render(request, "detalle_venta/crear.html", context)

@login_required
def detalle_venta_listar(request):
    titulo="Detalle Venta"
    modulo="ventas"
    detalles=Detalle_Venta.objects.all()
    context={
            "titulo":titulo,
            "detalles":detalles,
            "modulo":modulo
    }
    return render(request,"detalle_venta/listar.html", context)


@login_required
def detalle_venta_modificar(request,pk):
    titulo="Detalle Venta"
    mensaje = f'¡Hecho! El {titulo} se ha modificado exitosamente.'
    detalle_venta=Detalle_Venta.objects.get(id=pk)
    if request.method=='POST':
        form=Detalle_VentaUpdateForm(request.POST, instance=detalle_venta)
        if form.is_valid():
            form.save()
            return redirect('detalle_ventas')
    else:
        form=Detalle_VentaUpdateForm(instance=detalle_venta)
    context={"titulo":titulo,"form":form}
    return render(request,"detalle_venta/modificar.html", context)
