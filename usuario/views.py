from django.shortcuts import render,redirect
from usuario.forms import PersonaForm,PersonaUptadeForm
from usuario.forms import ContabilidadForm,ContabilidadUptadeForm
from usuario.forms import AporteForm,AporteUptadeForm
from usuario.forms import IpsForm,IpsUptadeForm
from usuario.forms import NominaForm,NominaUptadeForm
from usuario.forms import TrabajadorForm, TrabajadorUptadeForm
from usuario.models import Persona,Contabilidad,Aporte,Ips,Nomina,Trabajador

#CRUD PERSONA
def persona_crear(request):
    titulo="Persona"
    if request.method == 'POST':
        form=PersonaForm(request.POST)
        if form.is_valid():
            form.save()
        return redirect('personas')
    else:
        form=PersonaForm()
    context={
        "titulo":titulo,
        "form":form
    }
    return render(request,"persona/crear.html",context)

def persona_listar(request):
    titulo="Persona"
    personas=Persona.objects.all()
    context={
        "titulo":titulo,
        "personas":personas
    }
    return render(request,"persona/listar.html",context)

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

def persona_eliminar(request,pk):
    persona=Persona.objects.filter(id=pk)
    persona.update(
        estado="0"
    )
    return redirect('personas')

#CRUD Contabilidad
def contabilidad_crear(request):
    titulo="Contabilidad"
    if request.method == 'POST':
        form=ContabilidadForm(request.POST)
        if form.is_valid():
            form.save()
        return redirect('contabilidades')
    else:
        form=ContabilidadForm()
    context={
        "titulo":titulo,
        "form":form
    }
    return render(request,"contabilidad/crear.html",context)

def contabilidad_listar(request):
    titulo="contabilidad"
    Contabilidades=Contabilidad.objects.all()
    context={
        "titulo":titulo,
        "contabilidades":Contabilidades
    }
    return render(request,"Contabilidad/listar.html",context)

def contabilidad_modificar(request,pk):
    titulo="contabilidad"
    contabilidad=Contabilidad.objects.get(id=pk)
    if request.method=='POST':
        form=ContabilidadUptadeForm(request.POST,instance=contabilidad)
        if form.is_valid():
            form.save()
            return redirect('Contabilidades')
    else:
        form=ContabilidadUptadeForm(instance=contabilidad)
    context={
        "titulo":titulo,
        "form":form
    }
    return render (request,"contabilidad/modificar.html",context)

def contabilidad_eliminar(request,pk):
    contabiliadad=Contabilidad.objects.filter(id=pk)
    contabiliadad.update(
        estado="0"
    )
    return redirect('Contabilidades')

#CRUD Aporte
def aporte_crear(request):
    titulo="Aporte"
    if request.method == 'POST':
        form=AporteForm(request.POST)
        if form.is_valid():
            form.save()
        return redirect('aportes')
    else:
        form=AporteForm()
    context={
        "titulo":titulo,
        "form":form
    }
    return render(request,"aporte/crear.html",context)

def aporte_listar(request):
    titulo="Aporte"
    aportes=Aporte.objects.all()
    context={
        "titulo":titulo,
        "aportes":aportes
    }
    return render(request,"aporte/listar.html",context)

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

def aporte_eliminar(request,pk):
    aporte=Aporte.objects.filter(id=pk)
    aporte.update(
        estado="0"
    )
    return redirect('aportes')

#CRUD Ips
def ips_crear(request):
    titulo="Ips"
    if request.method == 'POST':
        form=IpsForm(request.POST)
        if form.is_valid():
            form.save()
        return redirect('ipss')
    else:
        form=IpsForm()
    context={
        "titulo":titulo,
        "form":form
    }
    return render(request,"ips/crear.html",context)

def ips_listar(request):
    titulo="Ips"
    ipss=Ips.objects.all()
    context={
        "titulo":titulo,
        "ipss":ipss
    }
    return render(request,"ips/listar.html",context)

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

def ips_eliminar(request,pk):
    ips=Ips.objects.filter(id=pk)
    ips.update(
        estado="0"
    )
    return redirect('ipss')

#CRUD Nomina
def nomina_crear(request):
    titulo="Nomina"
    if request.method == 'POST':
        form=NominaForm(request.POST)
        if form.is_valid():
            form.save()
        return redirect('nominas')
    else:
        form=NominaForm()
    context={
        "titulo":titulo,
        "form":form
    }
    return render(request,"nomina/crear.html",context)

def nomina_listar(request):
    titulo="Nomina"
    nominas=Nomina.objects.all()
    context={
        "titulo":titulo,
        "nominas":nominas
    }
    return render(request,"nomina/listar.html",context)

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

def nomina_eliminar(request,pk):
    nomina=Nomina.objects.filter(id=pk)
    nomina.update(
        estado="0"
    )
    return redirect('nominas')

#CRUD Trabajador
def trabajador_crear(request):
    titulo="Trabajador"
    if request.method == 'POST':
        form=TrabajadorForm(request.POST)
        if form.is_valid():
            form.save()
        return redirect('trabajadores')
    else:
        form=TrabajadorForm()
    context={
        "titulo":titulo,
        "form":form
    }
    return render(request,"trabajador/crear.html",context)

def trabajador_listar(request):
    titulo="Trabajador"
    trabajadores=Trabajador.objects.all()
    context={
        "titulo":titulo,
        "Trabajadores":trabajadores
    }
    return render(request,"trabajador/listar.html",context)
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


