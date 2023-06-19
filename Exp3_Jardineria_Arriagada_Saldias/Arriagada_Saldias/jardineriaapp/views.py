from django.shortcuts import render, redirect
from .models import *
from .forms import ProductoForm

# Create your views here.
def inicio(request):
    return render(request, '1_Inicio.html')

def sobrenosotros(request):
    return render(request, '2_SobreNosotros.html')

def productos(request):
    return render(request, '3_Productos.html')

def carrito(request):
    return render(request, '4_Carrito.html')

def datosenvio(request):
    return render(request, '5_DatosEnvio.html')

def escribenos(request):
    return render(request, '6_Escribenos.html')

def donaciones(request):
    return render(request, '7_Donaciones.html')

    
#Apartir de este texto estara todo lo relacionado al login y a la base de datos

def menustock(request):
    productos = Producto.objects.raw('Select * from jardineriaapp_producto')
    datos = {'items':productos}
    return render(request, '8_Stock.html', datos)

def crear(request):
    if request.method=='POST':
        productoform = ProductoForm(request.POST, request.FILES)
        if productoform.is_valid():
            productoform.save()     #similar al insert en función
            return redirect('menustock')
    else:
        productoform=ProductoForm()
    return render(request, '9_Crear.html',{'productoform': productoform})

def eliminar(request, id):
    productoEliminado=Producto.objects.get(codigo=id)  #obtenemos un objeto por su pk
    productoEliminado.delete()
    return redirect('menustock')

def modificar(request,id):
    producto = Producto.objects.get(codigo=id)         #obtenemos un objeto por su pk
    datos ={
        'form':ProductoForm(instance=producto)
    }
    if request.method=='POST':
        formulario = ProductoForm(data=request.POST, instance=producto)
        if formulario.is_valid:
            formulario.save()
            return redirect ('menustock')
    return render(request, '10_modificar.html', datos)