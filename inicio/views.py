from django.http import HttpResponse, HttpResponseBadRequest
from django.template import Template, Context, loader, RequestContext
from inicio.models import Frase, Aviso
from usuarios.models import User
from datetime import datetime

from django.shortcuts import render, redirect, get_object_or_404
from inicio.forms import CrearFraseFormulario, CrearAvisoFormulario, BuscarFrases
from django.contrib.auth.decorators import user_passes_test


def mi_vista(request):
    return render(request, 'inicio/index.html')

def about(request):
    return render(request, 'inicio/about.html')


def lista_frases(request):
    if not request.user.is_authenticated :
        lasfrases = Frase.objects.filter(privado__icontains=0 )
    else:
        lasfrases = Frase.objects.all()
    formulario_busqueda = BuscarFrases(request.GET)
    
    if formulario_busqueda.is_valid():
            palabra = formulario_busqueda.cleaned_data['palabra']
            lasfrases = lasfrases.filter(frase__icontains=palabra)
 
            


    return render(request, 'inicio/lista_frases.html', {'frases': lasfrases, 'formulario': formulario_busqueda})



def crear_frase(request):
    
    if request.method == "POST":
        formulario = CrearFraseFormulario(request.POST)
        
        if formulario.is_valid():
            datos_correctos = formulario.cleaned_data
        
            lafrase = Frase(nombre=datos_correctos['nombre'],edad=datos_correctos['edad'], frase=datos_correctos['frase'],privado=datos_correctos['privado'])
            lafrase.save()

            return redirect('inicio:crear_frase')
    
    formulario = CrearFraseFormulario()
    return render(request, 'inicio/crear_frase.html', {'formulario': formulario})


    

@user_passes_test(lambda u: u.is_superuser)

def editar_frase(request, id):
    frase = get_object_or_404(Frase,id=id)
    if request.method == 'POST':
        formulario = CrearFraseFormulario(request.POST, instance=frase)
        if formulario.is_valid():
            formulario.save()
            return redirect('inicio:lista_frases')
    else:
        
        formulario = CrearFraseFormulario(instance=frase)

    return render(request, 'inicio/editar_frase.html', { 'formulario': formulario, 'id':id})    


@user_passes_test(lambda u: u.is_superuser)
def eliminar_frase(request, id):
    frase = get_object_or_404(Frase, id=id)
    if request.method == 'POST':
        frase.delete()
        return redirect('inicio:lista_frases')
    return render(request, 'inicio/eliminar_frase.html', {'frase': frase})




def crear_aviso(request):
    
    if request.method == "POST":
        formulario = CrearAvisoFormulario(request.POST)
        
        if formulario.is_valid():
            datos_correctos = formulario.cleaned_data
        
            elaviso = Aviso(titulo=datos_correctos['titulo'],descripcion=datos_correctos['descripcion'])
            elaviso.save()

            return redirect('inicio:crear_aviso')
    
    formulario = CrearAvisoFormulario()
    return render(request, 'inicio/crear_aviso.html', {'formulario': formulario})

def lista_avisos(request):
    
    avisos = Aviso.objects.all()
    formulario_busqueda= CrearAvisoFormulario()
 
            
    return render(request, 'inicio/lista_avisos.html', {'avisos': avisos, 'formulario': formulario_busqueda})
