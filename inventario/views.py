from django.shortcuts import render,redirect
from inventario.forms import Materia_PrimaForm,Materia_PrimaUptadeForm,StockForm,StockUptadeForm
from inventario.models import Materia_Prima,Stock
from django.contrib import messages
# Create your views here.

#CRUD Materia Prima
def materia_prima_crear(request):
    titulo="Materia Prima"
    if request.method == 'POST':
        form=Materia_PrimaForm(request.POST)
        if form.is_valid():
            form.save()
            messages.success(request,'la Materia prima se a creado correctamente')
            return redirect('materias primas')
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
    titulo="Materia Prima"
    modulo="Stock"
    materia_primas=Materia_Prima.objects.all()
    context={
        "titulo":titulo,
        "modulo":modulo,
        "materias primas":materia_primas,
    }
    return render(request,"materia prima/listar.html",context)

def materia_prima_modificar(request,pk):
    titulo="Materia Prima"
    materia_prima=Materia_Prima.objects.get(id=pk)
    if request.method=='POST':
        form=Materia_PrimaUptadeForm(request.POST,instance=materia_prima)
        if form.is_valid():
            form.save()
            return redirect('materias primas')
    else:
        form=Materia_PrimaUptadeForm(instance=materia_prima)
    context={
        "titulo":titulo,
        "form":form
    }
    return render (request,"materia prima/modificar.html",context)

def materia_prima_eliminar(request,pk):
    materia_prima=Materia_Prima.objects.filter(id=pk)
    materia_prima.update(
        estado="0"
    )
    return redirect('materias primas')

#CRUD Stock
def stock_crear(request):
    titulo="Stock"
    if request.method == 'POST':
        form=StockForm(request.POST)
        if form.is_valid():
            form.save()
            messages.success(request,'la Materia prima se a creado correctamente')
            return redirect('materias primas')
        else:
            messages.error(request,'error revise los campos')

    else:
        form=StockForm()
    context={
        "titulo":titulo,
        "form":form
    }
    return render(request,"stock/crear.html",context)

def stock_listar(request):
    titulo="Materia Prima"
    modulo="Stock"
    stock=Stock.objects.all()
    context={
        "titulo":titulo,
        "modulo":modulo,
        "stocks":stock,
    }
    return render(request,"stock/listar.html",context)

def stock_modificar(request,pk):
    titulo="Stock"
    stock=Stock.objects.get(id=pk)
    if request.method=='POST':
        form=StockUptadeForm(request.POST,instance=stock)
        if form.is_valid():
            form.save()
            return redirect('Stocks')
    else:
        form=StockUptadeForm(instance=stock)
    context={
        "titulo":titulo,
        "form":form
    }
    return render (request,"stock/modificar.html",context)

def stock_eliminar(request,pk):
    stock=Stock.objects.filter(id=pk)
    stock.update(
        estado="0"
    )
    return redirect('Stocks')