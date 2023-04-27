from django.http import HttpResponse, HttpResponseBadRequest
from django.template import Template, Context, loader, RequestContext
from inicio.models import Frase, Moderador, Usuario
from django.shortcuts import render, redirect, get_object_or_404
from inicio.forms import CrearFraseFormulario, CrearModeradorFormulario, BuscarFrases, CrearUsuarioFormulario
from django.contrib.auth.decorators import user_passes_test


def mi_vista(request):
    return render(request, 'inicio/index.html')

def about(request):
    return render(request, 'inicio/about.html')


def lista_frases(request):
    buscar = request.GET.get('nombre', None)
    
    if buscar:
        mifrases = Frase.objects.filter(nombre__=buscar)
        
    else:
        mifrases = Frase.objects.filter(privado__icontains=0 )
    formulario_busqueda = BuscarFrases()
    return render(request, 'inicio/lista_frases.html', {'frases': mifrases, 'formulario': formulario_busqueda})



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

def crear_usuario(request):

        if request.method == "POST":
            formulario = CrearUsuarioFormulario(request.POST)
            
            if formulario.is_valid():
                datos_correctos = formulario.cleaned_data
            
                elusuario = Usuario(nombre=datos_correctos['nombre'],apellido=datos_correctos['apellido'], inhabilitado=0)
                elusuario.save()

        return redirect('inicio:crear_usuario')
    

@user_passes_test(lambda u: u.is_superuser)
def editar_frase(request, frase_id):
    frase = Frase.objects.get(id=frase_id)
    if request.method == 'POST':
        formulario = CrearFraseFormulario(request.POST, instance=frase)
        if formulario.is_valid():
            formulario.save()
            return redirect('inicio:lista_frases')
    else:
        formulario = CrearFraseFormulario(instance=frase, initial={'id': frase.id})
    context = {'frase': frase, 'formulario': formulario}
    return render(request, 'inicio/editar_frase.html', context)

@user_passes_test(lambda u: u.is_superuser)
def eliminar_frase(request, id_frase):
    frase = get_object_or_404(Frase, id=id_frase)
    if request.method == 'POST':
        frase.delete()
        return redirect('inicio:lista_frase')
    return render(request, 'inicio/eliminar_frase.html', {'frase': frase})


def crear_usuario(request):
    if request.method == "POST":
        formulario = CrearUsuarioFormulario(request.POST)
        
        if formulario.is_valid():
            datos_correctos = formulario.cleaned_data
        
            elusuario = Usuario(nombre=datos_correctos['nombre'],apellido=datos_correctos['apellido'], inhabilitado=0)
            elusuario.save()

            return redirect('inicio:crear_usuario')
    
    formulario = CrearUsuarioFormulario()
    return render(request, 'inicio/crear_usuario.html', {'formulario': formulario})

def crear_moderador(request):
    
    if request.method == "POST":
        formulario = CrearModeradorFormulario(request.POST)
        
        if formulario.is_valid():
            datos_correctos = formulario.cleaned_data
        
            elmoderador = Moderador(nombre=datos_correctos['nombre'],apellido=datos_correctos['apellido'], fecha_registro=datetime.now())
            elmoderador.save()

            return redirect('inicio:crear_frase')
    
    formulario = CrearModeradorFormulario()
    return render(request, 'inicio/crear_moderador.html', {'formulario': formulario})