from django.shortcuts import render, redirect
from venta.models import Venta, Detalle_Venta
from venta.forms import Detalle_VentaForm,Detalle_VentaUpdateForm,VentaForm,VentaUpdateForm
from django.contrib import messages
from django.contrib.auth.decorators import login_required

# Create your views here.
#VIEWS VENTA
#@login_required
def venta_crear(request):
    titulo="Venta"
    if request.method=='POST':
        form=VentaForm(request.POST)
        if form.is_valid():
            form.save()
            messages.success(request, 'Venta creada exitosamente. ')
            return redirect('ventas')
        else:
            messages.error(request, 'No se logro crear la venta intentelo de nuevo.')
    else:
        form=VentaForm()
    context={"titulo":titulo,"form":form}
    return render(request,"venta/crear.html", context)

#@login_required
def venta_listar(request):
    titulo="venta"
    venta=Venta.objects.all()
    context={"titulo":titulo,"venta":venta}
    return render(request,"venta/listar.html", context)

#@login_required
def venta_modificar(request,pk):
    titulo="Venta"
    venta=Venta.objects.get(id=pk)
    if request.method=='POST':
        form=VentaUpdateForm(request.POST, instance=venta)
        if form.is_valid():
            form.save()
            messages.success(request, 'La venta se ha modificado. ')
            return redirect('ventas')
    else:
        form=VentaUpdateForm(instance=venta)
    context={"titulo":titulo,"form":form}
    return render(request,"venta/modificar.html", context)

#@login_required
def venta_eliminar(request,pk):
    venta=Venta.objects.filter(id=pk)
    venta.update(estado="0")
    return redirect('ventas')

#VIEWS DETALLE_VENTA
#@login_required
def detalle_venta_crear(request):
    titulo="Detalle_Venta "
    if request.method=='POST':
        form=Detalle_VentaForm(request.POST)
        if form.is_valid():
            form.save()
            return redirect('detalle_ventas')
    else:
        form=Detalle_VentaForm()
    context={"titulo":titulo,"form":form}
    return render(request,"detalle_venta/crear.html", context)

#@login_required
def detalle_venta_listar(request):
    titulo="Detalle_Venta"
    detalles=Detalle_Venta.objects.all()
    context={
            "titulo":titulo,
            "detalles":detalles
    }
    return render(request,"detalle_venta/listar.html", context)

#@login_required
def detalle_venta_modificar(request,pk):
    titulo="Detalle_Venta"
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
