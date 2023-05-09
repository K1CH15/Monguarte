from django.shortcuts import render, redirect
from productos.models import Producto,Tamaño,Tipo
from productos.forms import ProductoForm,ProductoUpdateForm,TamañoForm, TamañoUpdateForm,TipoForm,TipoUpdateForm
from django.contrib import messages
# Create your views here.
def producto_crear(request):
    titulo="Producto"
    if request.method== 'POST':
        form= ProductoForm(request.POST)
        if form.is_valid():
            form.save()
            messages.success(request, 'El formulario se ha enviado correctamente.')

            return redirect('productos')
        else:
            messages.error(request, 'El formulario tiene errores.')
    else:
        form= ProductoForm()
    context={
        "titulo":titulo,
        "form":form
        }
    return render(request,"productos/crear.html", context)

def producto_listar(request):
    titulo="Producto"
    modulo="Productos"
    productosn= Producto.objects.all()
    context={
        "titulo":titulo,
        "modulo":modulo,
        "productosn":productosn
    }
    return render(request,"productos/listar.html", context)

def producto_modificar(request,pk):
    titulo="Usuario"
    producto= Producto.objects.get(id=pk)
    
    if request.method== 'POST':
        form= ProductoUpdateForm(request.POST, instance=producto)
        if form.is_valid():
            form.save()
            messages.success(request, 'El formulario se ha enviado correctamente.')
            return redirect('productos')
    else:
        form= ProductoUpdateForm(instance=producto)
    context={
        "titulo":titulo,
        "form":form
        }
    return render(request,"productos/modificar.html", context)

def producto_eliminar(request,pk):
    producto= Producto.objects.filter(id=pk)
    producto.update(
        estado="0"
    )
    return redirect('productos')


def tamaño_crear(request):
    titulo="Tamaño"
    if request.method== 'POST':
        form= TamañoForm(request.POST)
        if form.is_valid():
            form.save()
            messages.success(request, 'correcto,el formulario esta completado')

            return redirect('tamaños')
        else:
            messages.error(request, 'El formulario  de tamañotiene errores.')
    else:
        form= TamañoForm()
    context={
        "titulo":titulo,
        "form":form
        }
    return render(request,"tamaños/crear.html", context)

def tamaño_listar(request):
    titulo="Tamaño"
    modulo="Productos"
    tamaños= Tamaño.objects.all()
    context={
        "titulo":titulo,
        "modulo":modulo,
        "tamaños":tamaños,
    }
    return render(request,"tamaños/listar.html", context)

def tamaño_modificar(request,pk):
    titulo="Tamaño"
    tamaño= Tamaño.objects.get(id=pk)
    
    if request.method== 'POST':
        form= TamañoUpdateForm(request.POST, instance=tamaño)
        if form.is_valid():
            form.save()
            messages.success(request, 'El formulario se ha enviado correctamente.')
            return redirect('tamaños')   
        else:
            messages.error(request, 'Error Al Modificar La Compra')
    else:
        form= TamañoUpdateForm(instance=tamaño)
    context={
        "titulo":titulo,
        "form":form
        }
    return render(request,"tamaños/modificar.html", context)

def tamaño_eliminar(request,pk):
    tamaño= Tamaño.objects.filter(id=pk)
    tamaño.update(
        estado="0"
    )
    return redirect('tamaños')




  
def tipo_crear(request):
    titulo="Tipo"
    if request.method== 'POST':
        form= TipoForm(request.POST)
        if form.is_valid():
            form.save()
            messages.success(request, 'El formulario de tipo se ha enviado correctamente.')
            return redirect('tipos')
        else:
            messages.error(request, 'El formulario  de tipo tiene errores.')
    else:
        form= TipoForm()
    context={
        "titulo":titulo,
        "form":form
        }
    return render(request,"tipos/crear.html", context)

def tipo_listar(request):
    titulo="Tipo"
    modulo="productos"
    tipos= Tipo.objects.all()
    context={
        "titulo":titulo,
        "modulo":modulo,
        "tipos":tipos
    }
    return render(request,"tipos/listar.html", context)

def tipo_modificar(request,pk):
    titulo="Tipo"
    
    tipo= Tipo.objects.get(id=pk)
    
    if request.method== 'POST':
        form= TipoUpdateForm(request.POST, instance=tipo)
        if form.is_valid():
            form.save()
            return redirect('tipos')
    else:
        form= TipoUpdateForm(instance=tipo)
    context={
        "titulo":titulo,
        "form":form
        }
    return render(request,"tipos/modificar.html", context)
def tipo_eliminar(request,pk):
    tipo= Tipo.objects.filter(id=pk)
    tipo.update(
        estado="0"
    )
    return redirect('tipos')