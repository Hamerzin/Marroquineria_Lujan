from re import template
from django.shortcuts import render
from django.shortcuts import redirect, render, HttpResponse
from django.urls import reverse_lazy
from django.views.generic import ListView
from django.views.generic.detail import DetailView
from django.views.generic.edit import CreateView, UpdateView, DeleteView
from appblog.models import *
from django.contrib.auth.forms import AuthenticationForm, UserCreationForm
from django.contrib.auth.decorators import login_required
from appblog.forms import *

from django.db.models import Q
# -----INICIO DE CRUD MEDIANTE CBV -----
 
@method_decorator(staff_member_required, name='dispatch')
class ProductosCreacion(CreateView):
    model=Productos
    template_name="crear_productos.html"
    fields = ['tipo', 'nombre','imagen','precio', 'codigo','stock','detalle']
    success_url=reverse_lazy('administracion')
    
@method_decorator(staff_member_required, name='dispatch')
class ProductosEditar(UpdateView):
    model=Productos
    template_name="edit_form.html"
    fields = ['tipo', 'nombre','imagen','precio', 'codigo','stock','detalle']
    success_url=reverse_lazy('administracion') 
    
@method_decorator(staff_member_required, name='dispatch')
class ProductosDelete(DeleteView):
    model=Productos
    template_name="profesor_confirm_delete.html"
    success_url=reverse_lazy('administracion')
    
class ProductoDetalle(DetailView):
      model=Productos
      template_name="detalles.html"

#----FIN DE CRUD------------------------------------------------

def productos(request):
      return render(request, "login2.html")


def verproductoss(request): 
      prods = Productos.objects.all()

      return render (request, 'product.html', {'prods':prods})

@login_required()

def administracion(request): 
      
       if not request.user.is_staff:
        #redirect('/')
        #return render(request, 'restricted.html')
        return render(request, "accesodenegado.html")

       else:
            prods = Productos.objects.all()
            return render (request, 'vistaproductos.html', {'prods':prods})


    
def buscar(request):
      if request.method=="POST":
            search = request.POST['search']
            print(search)
            if search !="":
                  resultados="Resultados para:"
                  prods = Productos.objects.filter(Q(nombre__icontains=search)|Q(tipo__icontains=search)|Q(codigo__icontains=search))
                  return render(request, "tienda.html", {"productos": prods, "nombre":search, "search":True, "resultados":resultados} )
                                 
            else:
             output = "No ingresaste ningun dato"
             return render(request, "tienda.html", {'mensaje':output})
    

def buscarprods(request):
      return render(request, 'buscarprods.html')


def buscartipo(request):
            
            prods = Productos.objects.filter(tipo__icontains="accesorios")
            vista="RESULTADOS EN CATEGORIA ACCESORIOS"
            return render(request, "tienda.html", {"productos": prods, "vista":vista} )
           
def buscartipoliq(request):
            
            prods = Productos.objects.filter(tipo__icontains="liquidaciones")
            vista="RESULTADOS EN CATEGORIA LIQUIDACIONES"
            return render(request, "tienda.html", {"productos": prods, "vista":vista} )

      
          

                        
def buscarmochilas(request):
            
            prods = Productos.objects.filter(tipo__icontains="Mochila")
            return render(request, "tienda.html", {"productos": prods} )
 
def buscarmarro(request):
            
            prods = Productos.objects.filter(tipo__icontains="Marroquineria")
            vista="RESULTADOS EN CATEGORIA MARROQUINERIA"
            return render(request, "tienda.html", {"productos": prods, "vista":vista} )

            return render(request, "tienda.html", {"productos": prods} )      

