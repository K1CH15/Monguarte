from django.shortcuts import render,redirect
from django.contrib import messages
from django.contrib.auth.decorators import login_required
from usuario.forms import PersonaForm,PersonaUptadeForm
from usuario.forms import ContabilidadForm,ContabilidadUptadeForm
from usuario.forms import AporteForm,AporteUptadeForm
from usuario.forms import IpsForm,IpsUptadeForm
from usuario.forms import NominaForm,NominaUptadeForm
from usuario.forms import TrabajadorForm, TrabajadorUptadeForm
from usuario.models import Persona,Contabilidad,Aporte,Ips,Nomina,Trabajador

#CRUD PERSONA
##@login_required
def persona_crear(request):
    titulo="Persona"
    if request.method == 'POST':
        form=PersonaForm(request.POST)
        if form.is_valid():
            form.save()
            messages.success(request,'la persona se a creado correctamente')
            return redirect('personas')
        else:
            messages.error(request,'error revise los campos')

    else:
        form=PersonaForm()
    context={
        "titulo":titulo,
        "form":form
    }
    return render(request,"persona/crear.html",context)

##@login_required
def persona_listar(request):
    titulo="persona"
    modulo="usuarios"
    personas=Persona.objects.all()
    context={
        "titulo":titulo,
        "modulo":modulo,
        "personas":personas,

    }
    return render(request,"persona/listar.html",context)

##@login_required
def persona_modificar(request,pk):
    titulo="Persona"
    persona=Persona.objects.get(id=pk)
    if request.method=='POST':
        form=PersonaUptadeForm(request.POST,instance=persona)
        if form.is_valid():
            form.save()
            return redirect('personas')
    else:
        form=PersonaUptadeForm(instance=persona)
    context={
        "titulo":titulo,
        "form":form
    }
    return render (request,"persona/modificar.html",context)

##@login_required
def persona_eliminar(request,pk):
    persona=Persona.objects.filter(id=pk)
    persona.update(
        estado="0"
    )
    return redirect('personas')

#CRUD Contabilidad
##@login_required
def contabilidad_crear(request):
    titulo="Contabilidad"
    if request.method == 'POST':
        form=ContabilidadForm(request.POST)
        if form.is_valid():
            form.save()
            messages.success(request,'se creado exitosamente')
            return redirect('contabilidades')
        else:
            messages.error(request,'error en los campos')
    else:
        form=ContabilidadForm()
    context={
        "titulo":titulo,
        "form":form
    }
    return render(request,"contabilidad/crear.html",context)

##@login_required
def contabilidad_listar(request):
    titulo="contabilidad"
    modulo="usuarios"
    Contabilidades=Contabilidad.objects.all()
    context={
        "titulo":titulo,
        "contabilidades":Contabilidades,
        "modulo":modulo,
        
    }
    return render(request,"contabilidad/listar.html",context)

##@login_required
def contabilidad_modificar(request,pk):
    titulo="contabilidad"
    contabilidad=Contabilidad.objects.get(id=pk)
    if request.method=='POST':
        form=ContabilidadUptadeForm(request.POST,instance=contabilidad)
        if form.is_valid():
            form.save()
            return redirect('contabilidades')
    else:
        form=ContabilidadUptadeForm(instance=contabilidad)
    context={
        "titulo":titulo,
        "form":form
    }
    return render (request,"contabilidad/modificar.html",context)

##@login_required
def contabilidad_eliminar(request,pk):
    contabiliadad=Contabilidad.objects.filter(id=pk)
    contabiliadad.update(
        estado="0"
    )
    return redirect('contabilidades')

#CRUD Aporte
##@login_required
def aporte_crear(request):
    titulo="Aporte"
    if request.method == 'POST':
        form=AporteForm(request.POST)
        if form.is_valid():
            form.save()
            messages.success(request,'se creado exitosamente')
            return redirect('aportes')
        else:
            messages.error(request,'error en los campos')
    else:
        form=AporteForm()
    context={
        "titulo":titulo,
        "form":form
    }
    return render(request,"aporte/crear.html",context)

##@login_required
def aporte_listar(request):
    titulo="Aporte"
    modulo="usuarios"
    aportes=Aporte.objects.all()
    context={
        "titulo":titulo,
        "modulo":modulo,
        "aportes":aportes,
        
    }
    return render(request,"aporte/listar.html",context)

##@login_required
def aporte_modificar(request,pk):
    titulo="Aporte"
    aporte=Aporte.objects.get(id=pk)
    if request.method=='POST':
        form=AporteUptadeForm(request.POST,instance=aporte)
        if form.is_valid():
            form.save()
        return redirect('aportes')
    else:
        form=AporteUptadeForm(instance=aporte)
    context={
        "titulo":titulo,
        "form":form
    }
    return render (request,"aporte/modificar.html",context)

##@login_required
def aporte_eliminar(request,pk):
    aporte=Aporte.objects.filter(id=pk)
    aporte.update(
        estado="0"
    )
    return redirect('aportes')

#CRUD Ips
##@login_required
def ips_crear(request):
    titulo="Ips"
    if request.method == 'POST':
        form=IpsForm(request.POST)
        if form.is_valid():
            form.save()
            messages.success(request,'se creado exitosamente')
            return redirect('ipss')
        else:
            messages.error(request,'error en los campos')
    else:
        form=IpsForm()
    context={
        "titulo":titulo,
        "form":form
    }
    return render(request,"ips/crear.html",context)

##@login_required
def ips_listar(request):
    titulo="Ips"
    modulo="usuario"
    ipss=Ips.objects.all()
    context={
        "titulo":titulo,
        "ipss":ipss,
        "modulo":modulo,
    }
    return render(request,"ips/listar.html",context)

##@login_required
def ips_modificar(request,pk):
    titulo="Ips"
    ips=Ips.objects.get(id=pk)
    if request.method=='POST':
        form=IpsUptadeForm(request.POST,instance=ips)
        if form.is_valid():
            form.save()
            return redirect('ipss')
    else:
        form=IpsUptadeForm(instance=ips)
    context={
        "titulo":titulo,
        "form":form
    }
    return render (request,"ips/modificar.html",context)

##@login_required
def ips_eliminar(request,pk):
    ips=Ips.objects.filter(id=pk)
    ips.update(
        estado="0"
    )
    return redirect('ipss')

#CRUD Nomina
##@login_required
def nomina_crear(request):
    titulo="Nomina"
    if request.method == 'POST':
        form=NominaForm(request.POST)
        if form.is_valid():
            form.save()
            messages.success(request,'se creado exitosamente')
            return redirect('nominas')
        else:
            messages.error(request,'error en los campos')
    else:
        form=NominaForm()
    context={
        "titulo":titulo,
        "form":form
    }
    return render(request,"nomina/crear.html",context)

##@login_required
def nomina_listar(request):
    titulo="Nomina"
    modulo="usuarios"
    nominas=Nomina.objects.all()
    context={
        "titulo":titulo,
        "modulo":modulo,
        "nominas":nominas,
    }
    return render(request,"nomina/listar.html",context)

##@login_required
def nomina_modificar(request,pk):
    titulo="Nomina"
    nomina=Nomina.objects.get(id=pk)
    if request.method=='POST':
        form=NominaUptadeForm(request.POST,instance=nomina)
        if form.is_valid():
            form.save()
            return redirect('nominas')
    else:
        form=NominaUptadeForm(instance=nomina)
    context={
        "titulo":titulo,
        "form":form
    }
    return render (request,"nomina/modificar.html",context)

##@login_required
def nomina_eliminar(request,pk):
    nomina=Nomina.objects.filter(id=pk)
    nomina.update(
        estado="0"
    )
    return redirect('nominas')

#CRUD Trabajador
##@login_required
def trabajador_crear(request):
    titulo="Trabajador"
    if request.method == 'POST':
        form=TrabajadorForm(request.POST)
        if form.is_valid():
            form.save()
            messages.success(request,'se creado exitosamente')
            return redirect('trabajadores')
        else:
            messages.error(request,'error en los campos')
    else:
        form=TrabajadorForm()
    context={
        "titulo":titulo,
        "form":form
    }
    return render(request,"trabajador/crear.html",context)

##@login_required
def trabajador_listar(request):
    titulo="trabajador"
    modulo="usuarios"
    trabajadores=Trabajador.objects.all()
    context={
        "titulo":titulo,
        "modulo":modulo,
        "trabajadores":trabajadores,

    }
    return render(request,"trabajador/listar.html",context)

##@login_required
def trabajador_modificar(request,pk):
    titulo="Trabajador"
    trabajador=Trabajador.objects.get(id=pk)
    if request.method=='POST':
        form=TrabajadorUptadeForm(request.POST,instance=trabajador)
        if form.is_valid():
            form.save()
            return redirect('trabajadores')
    else:
        form=TrabajadorUptadeForm(instance=trabajador)
    context={
        "titulo":titulo,
        "form":form
    }
    return render (request,"trabajador/modificar.html",context)


