from django.shortcuts import render
from django.shortcuts import render, HttpResponse, redirect
from django.views.generic.edit import CreateView
from django.urls import reverse_lazy
from Carrito.Carrito import Carrito
from Carrito.models import CarritoModel
from appblog.models import Productos
from django.contrib.auth.decorators import login_required
from Carrito.context_processor import total_carrito



def tienda(request):
    #return HttpResponse("Hola Pythonizando")
    productos = Productos.objects.all()
    return render(request, "tienda.html", {'productos':productos})
@login_required
def agregar_producto(request, producto_id):
    carrito = Carrito(request)
    producto = Productos.objects.get(id=producto_id)
    carrito.agregar(producto)
    return redirect("Tienda")

def agregar_producto2(request, producto_id):
    carrito = Carrito(request)
    producto = Productos.objects.get(id=producto_id)
    carrito.agregar(producto)
    return redirect("detalle")

def eliminar_producto(request, producto_id):
    carrito = Carrito(request)
    producto =Productos.objects.get(id=producto_id)
    carrito.eliminar(producto)
    return redirect("detalle")

def restar_producto(request, producto_id):
    carrito = Carrito(request)
    producto = Productos.objects.get(id=producto_id)
    carrito.restar(producto)
    return redirect("detalle")

def limpiar_carrito(request):
    carrito = Carrito(request)
    carrito.limpiar()
    return redirect("detalle")

def detalle_carrito(request):
    return render(request, "carrito_detalle.html")

    

def checkout(request):
	return render(request, 'checkout.html')

