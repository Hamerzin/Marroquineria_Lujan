from ast import Return
from distutils.command.upload import upload
from django.db import models
from django.contrib.auth.models import User
from django.forms import IntegerField
from django.shortcuts import redirect
from django.template.defaultfilters import slugify
from django.urls import reverse_lazy
from django.utils.decorators import method_decorator
from django.contrib.admin.views.decorators import staff_member_required

    
class Productos(models.Model):
    
    codigo=models.IntegerField(default=00000)
    tipo=models.CharField(max_length=50)
    nombre=models.CharField(max_length=50)
    imagen=models.ImageField(upload_to='imgproductos',null=True,blank=True)
    imagen2=models.ImageField(upload_to='imgproductos',null=True,blank=True)
    imagen3=models.ImageField(upload_to='imgproductos',null=True,blank=True)
    imagen4=models.ImageField(upload_to='imgproductos',null=True,blank=True)
    imagen5=models.ImageField(upload_to='imgproductos',null=True,blank=True)
    imagen6=models.ImageField(upload_to='imgproductos',null=True,blank=True)
    precio=models.IntegerField()
    stock=models.IntegerField(default=0)
    detalle=models.TextField(max_length=1000, default="ingresa detalle de producto")
    def __str__(self):
        return f"Codigo: {self.codigo} - Tipo de Producto {self.tipo} - Nombre {self.nombre} - Precio {self.precio} - Stock {self.stock} - Imagen {self.imagen}- Detalle {self.detalle}"

class StaffRequiredmixin():
    """
    Clase para bloquear acceso a usuarios que no sean del staff
    """
    @method_decorator(staff_member_required)
    def dispatch(self,request,*args, **kwargs):
        if not request.user.is_staff:
            return redirect(reverse_lazy('admin:login'))
        return super(StaffRequiredmixin, self).dispatch(request, *args, **kwargs)
        
