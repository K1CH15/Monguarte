from django.shortcuts import render,redirect
from inventario.forms import Materia_PrimaForm,Materia_PrimaUptadeForm
from inventario.forms import Stock_Materia_PrimaForm,Stock_Materia_PrimaUptadeForm
from inventario.forms import Stock_ProductoForm,Stock_ProductoUptadeForm
from inventario.models import Materia_Prima,Stock_Materia_Prima,Stock_Producto
from django.contrib import messages
# Create your views here.

#CRUD Materia Prima
def materia_prima_crear(request):
    titulo="materia prima"
    if request.method == 'POST':
        form=Materia_PrimaForm(request.POST)
        if form.is_valid():
            form.save()
            messages.success(request,'la Materia prima se a creado correctamente')
            return redirect('')
        else:
            messages.error(request,'error revise los campos')

    else:
        form=Materia_PrimaForm()
    context={
        "titulo":titulo,
        "form":form
    }
    return render(request,"materia prima/crear.html",context)

def materia_prima_listar(request):
    titulo="materia prima"
    modulo="inventario"
    materia_primas=Materia_Prima.objects.all()
    context={
        "titulo":titulo,
        "modulo":modulo,
        "materias primas":materia_primas,
    }
    return render(request,"materia prima/listar.html",context)

def materia_prima_modificar(request,pk):
    titulo="materia prima"
    materia_prima=Materia_Prima.objects.get(id=pk)
    if request.method=='POST':
        form=Materia_PrimaUptadeForm(request.POST,instance=materia_prima)
        if form.is_valid():
            form.save()
            return redirect('')
    else:
        form=Materia_PrimaUptadeForm(instance=materia_prima)
    context={
        "titulo":titulo,
        "form":form
    }
    return render (request,"/modificar.html",context)

def materia_prima_eliminar(request,pk):
    materia_prima=Materia_Prima.objects.filter(id=pk)
    materia_prima.update(
        estado="0"
    )
    return redirect('')

#CRUD Stock_Materia_Prima
def stock_materia_prima_crear(request):
    titulo="stock materia prima"
    if request.method == 'POST':
        form=Stock_Materia_Prima(request.POST)
        if form.is_valid():
            form.save()
            messages.success(request,'la Materia prima se a creado correctamente')
            return redirect('')
        else:
            messages.error(request,'error revise los campos')
    else:
        form=Stock_Materia_PrimaForm()
    context={
        "titulo":titulo,
        "form":form
    }
    return render(request,"/crear.html",context)

def stock_materia_prima_listar(request):
    titulo="stock materia prima"
    modulo="inventario"
    stock_materia_prima=Stock_Materia_Prima.objects.all()
    context={
        "titulo":titulo,
        "modulo":modulo,
        "stocks":stock_materia_prima,
    }
    return render(request,"stock materia prima/listar.html",context)

def stock_materia_prima_modificar(request,pk):
    titulo="stock materia prima"
    stock_materia_prima=Stock_Materia_Prima.objects.get(id=pk)
    if request.method=='POST':
        form=Stock_Materia_PrimaUptadeForm(request.POST,instance=stock_materia_prima)
        if form.is_valid():
            form.save()
            return redirect('')
    else:
        form=Stock_Materia_Prima(instance=stock_materia_prima)
    context={
        "titulo":titulo,
        "form":form
    }
    return render (request,"/modificar.html",context)

def stock_materia_prima_eliminar(request,pk):
    stock_materia_prima=Stock_Materia_Prima.objects.filter(id=pk)
    stock_materia_prima.update(
        estado="0"
    )
    return redirect('')
#CRUD Stock_Producto
def stock_producto_crear(request):
    titulo="stock producto"
    if request.method == 'POST':
        form=Stock_Producto(request.POST)
        if form.is_valid():
            form.save()
            messages.success(request,'falta')
            return redirect('')
        else:
            messages.error(request,'xd')
    else:
        form=Stock_ProductoForm()
    context={
        "titulo":titulo,
        "form":form
    }
    return render(request,"/crear.html",context)

def stock_producto_listar(request):
    titulo="stock producto"
    modulo="inventario"
    stock_producto=Stock_Producto.objects.all()
    context={
        "titulo":titulo,
        "modulo":modulo,
        "stocks":stock_producto,
    }
    return render(request,"/listar.html",context)

def stock_producto_modificar(request,pk):
    titulo="stock producto"
    stock_producto=Stock_Producto.objects.get(id=pk)
    if request.method=='POST':
        form=Stock_ProductoUptadeForm(request.POST,instance=stock_producto)
        if form.is_valid():
            form.save()
            return redirect('')
    else:
        form=Stock_Materia_Prima(instance=stock_producto)
    context={
        "titulo":titulo,
        "form":form
    }
    return render (request,"/modificar.html",context)

def stock_producto_eliminar(request,pk):
    stock_producto=Stock_Producto.objects.filter(id=pk)
    stock_producto.update(
        estado="0"
    )
    return redirect('')
