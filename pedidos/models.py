from tabnanny import verbose
from django.contrib.auth import get_user_model, get_user
from django.db import models
from appblog.models import Productos
from django.db.models import F, Sum, FloatField
from django.conf import settings


# Create your models here.
User=settings.AUTH_USER_MODEL

class Pedido(models.Model):
    user=models.ForeignKey(User, on_delete=models.CASCADE)
    created_at=models.DateTimeField(auto_now_add=True)

    def __str__(self):
        return str(self.id)

    @property
    def total(self):
        return self.lineapedido_set.aggregate(
            total=Sum(F("precio")*F("cantidad"), output_field=FloatField())
        )


    class Meta:
        db_table='pedidos'
        verbose_name='pedido'
        verbose_name_plural='pedidos'
        ordering=["id"]

class lineapedido(models.Model):

    user=models.ForeignKey(User,on_delete=models.CASCADE)
    producto=models.ForeignKey(Productos,on_delete=models.CASCADE)
    pedido=models.ForeignKey(Pedido,on_delete=models.CASCADE)
    cantidad=models.IntegerField(default=1)
    created_at=models.DateTimeField(auto_now_add=True)
    imagen=models.ImageField()
    total=models.FloatField(default=0)
    precio=models.IntegerField(default=0)
    nombre=models.CharField(max_length=200, null=False, default="")

    def __str__(self):
        return f'{str(self.cantidad)} Unidades de {self.producto.nombre}'

    class Meta:
       db_table='lineapedidos'
       verbose_name='Linea pedido'
       verbose_name_plural='Lineas pedidos'
       ordering=["id"]

class ShippingAddress(models.Model):
    customer = models.ForeignKey(User, on_delete=models.SET_NULL, null=True)
    order = models.ForeignKey(Pedido, on_delete=models.SET_NULL, null=True)
    address = models.CharField(max_length=200, null=False)
    city = models.CharField(max_length=200, null=False)
    state = models.CharField(max_length=200, null=False)
    zipcode = models.CharField(max_length=200, null=False)
    date_added = models.DateTimeField(auto_now_add=True)
    telefono = models.BigIntegerField()
    country=models.CharField(max_length=200, null=False, default="argentina")
  
    
    def __str__(self):
        return self.address
    
