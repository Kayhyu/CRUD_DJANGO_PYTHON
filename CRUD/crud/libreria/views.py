from django.shortcuts import render, redirect
from django.http import HttpResponse # para que le muestres al usuario
from .models import libro
from .forms import libroForm

# Create your views here.
def inicio(request): #creano funcion, que nos mostrraá el mensaje
     return render(request,'paginas/inicio.html')

def nosotros(request):
    #busca con a ese archivo
    return render(request,'paginas/nosotros.html')

def libros(request):
    libros=libro.objects.all()
    #print(libros)#para mostrar informacion por consola, veifcar
    #busca con a ese archivo
    return render(request,'libros/index.html',{'libros' :libros })

def crear(request):
    formulario=libroForm(request.POST or None, request.FILES or None)
    if formulario.is_valid():
        formulario.save()
        return redirect('libros')
    return render(request,'libros/crear.html',{'formulario' :formulario })

def editar(request,id):
    libros=libro.objects.get(id=id)
    formulario=libroForm(request.POST or None, request.FILES or None, instance=libros)
    if formulario.is_valid() and request.POST:
        formulario.save()
        return redirect('libros')
    #busca con a ese archivo
    return render(request,'libros/editar.html',{'formulario' :formulario })
 
def eliminar(request,id):
    #busca con a ese archivo
    libros=libro.objects.get(id=id)
    libros.delete()
    return redirect('libros')