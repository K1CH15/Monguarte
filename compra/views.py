from django.shortcuts import render, redirect
from compra.models import Compra,Detalle_Compra
from compra.forms import CompraForm,CompraUpdateForm,Detalle_CompraForm,Detalle_CompraUpdateForm
from django.contrib import messages
import os
from dbbackup.management.commands.dbbackup import Command as DbBackupCommand
from django.contrib.auth.decorators import login_required
# Create your views here.
# Creación COMPRA crear,listar,modificar,eliminar


#backup
def hacer_backup(request):
    #Ruta donde desea guardar el archivo de backup (asegurate de que ña carpeta "backups2 exista)
    backup_dir = os.path.join(os.path.dirname(os.path.dirname(os.path.abspath(__file__))),'base','backups')
    backup_file =f'{backup_dir}/nombre_del_archivo.bak'

    # Logica para realizar el backup aqui
    verbosity_level= 1 #Establece un valor entero para verbosity, p. ej. 1
    DbBackupCommand().handle(filename=backup_file, verbosity=verbosity_level)

    return redirect('compra')

def compra_crear(request):
    titulo = "Compra"
    compra = Compra.objects.all()  # Obtén las compras desde la base de datos

    if request.method == 'POST':
        form = CompraForm(request.POST)
        if form.is_valid():
            form.save()
            messages.success(request, 'La Compra Se Agregó Correctamente')
            return redirect('compra')
        else:
            messages.error(request, '¡Oops! Parece que ha ocurrido un error en el formulario. Te pedimos que revises los campos resaltados y realices las correcciones necesarias.')
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
    titulo="compra"
    modulo="compras"
    compra = Compra.objects.all()
    context={
        "titulo":titulo,
        "modulo":modulo,
        "compra":compra,
    }
    return render(request,"compra/listar.html", context)

@login_required
def compra_modificar(request,pk):
    titulo="Compra"
    compra= Compra.objects.get(id=pk)

    if request.method== 'POST':
        form= CompraUpdateForm(request.POST, instance=compra)
        if form.is_valid():
            form.save()
            messages.success(request, 'Se Modifico Correctamente La Compra')
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

@login_required
def compra_eliminar(request,pk):
    compra= Compra.objects.filter(id=pk)
    compra.update(
        estado="0"
    )
    return redirect('compra')

#Creación DETALLE COMPRA
@login_required
def detalle_compra_crear(request):
    titulo = "Detalle Compra Crear"
    comprasn = Compra.objects.all()  # Obtén las compras desde la base de datos

    if request.method == 'POST':
        form = Detalle_CompraForm(request.POST)
        if form.is_valid():
            form.save()
            messages.success(request, 'El detalle de compra se ha agregado correctamente')
            return redirect('detalle_compra')
        else:
            messages.error(request, '¡Oops! Parece que ha ocurrido un error en el formulario. '
                                    'Te pedimos que revises los campos resaltados y realices las correcciones necesarias.')
    else:
        form = Detalle_CompraForm()

    context = {
        "titulo": titulo,
        "comprasn": comprasn,
        "form": form  # Agrega el formulario al contexto
    }

    return render(request, "detalle_compra/crear.html", context)

@login_required
def detalle_compra_listar(request):
    titulo="Detalle_compra"
    detalle_compras= Detalle_Compra.objects.all()
    context={
        "titulo":titulo,

        "detalle_compras":detalle_compras
    }
    return render(request,"detalle_compra/listar.html", context)

@login_required
def detalle_compra_modificar(request,pk):
    titulo="Detalle_compra"
    detalle_compra = Detalle_Compra.objects.get(id=pk)

    if request.method== 'POST':
        form= Detalle_CompraUpdateForm(request.POST, instance=detalle_compra)
        if form.is_valid():
            form.save()
            messages.success(request, 'Se Modifico Correctamente El Detalle Compra')
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

