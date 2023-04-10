from django.shortcuts import render, redirect
from venta.models import Venta
from venta.forms import Detalle_VentaForm,Detalle_VentaUpdateForm,VentaForm,VentaUpdateForm
# Create your views here.
#VIEWS VENTA
def venta_crear(request):
    titulo="Venta"
    if request.method=='POST':
        form=VentaForm(request.POST)
        if form.is_valid():
            form.save()
            return redirect('ventas')
    else:
        form=VentaForm()
    context={"titulo":titulo,"form":form}
    return render(request,"venta/crear.html", context)

def venta_listar(request):
    titulo="venta"
    venta=Venta.objects.all()
    context={"titulo":titulo,"venta":venta}
    return render(request,"venta/listar.html", context)

def venta_modificar(request,pk):
    titulo="Venta"
    venta=Venta.objects.get(id_venta=pk)
    if request.method=='POST':
        form=VentaUpdateForm(request.POST, instance=venta)
        if form.is_valid():
            form.save()
            return redirect('ventas')
    else:
        form=VentaUpdateForm()
    context={"titulo":titulo,"form":form}
    return render(request,"venta/modificar.html", context)

def venta_eliminar(request,pk):
    venta=Venta.object.filter(id_venta=pk)
    venta.update(estado="0")
    return redirect('ventas')

#VIEWS DETALLE_VENTA
def detalle_venta_crear(request):
    titulo="Detalle_Venta "
    if request.method=='POST':
        form=Detalle_VentaForm(request.POST)
        if form.is_valid():
            form.save()
            return redirect('detalle_venta')
    else:
        form=Detalle_VentaForm()
    context={"titulo":titulo,"form":form}
    return render(request,"detalle_venta/crear.html", context)

def detalle_venta_listar(request):
    titulo="Detalle_Venta"
    detalle_venta=Venta.objects.all()
    context={"titulo":titulo,"detalle_venta":detalle_venta}
    return render(request,"detalle_venta/listar.html", context)

def detalle_venta_modificar(request,pk):
    titulo="Detalle_Venta"
    detalle_venta=Venta.objects.get(id_detalle_venta=pk)
    if request.method=='POST':
        form=Detalle_VentaUpdateForm(request.POST, instance=detalle_venta)
        if form.is_valid():
            form.save()
            return redirect('venta')
    else:
        form=Detalle_VentaUpdateForm()
    context={"titulo":titulo,"form":form}
    return render(request,"detalle_venta/modificar.html", context)
