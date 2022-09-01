from django.urls import URLPattern, path

#cosas para el login
from django.contrib.auth.views import LogoutView
from django.views import View
from Carrito import views
from Carrito.views import *


urlpatterns = [
    path('', views.tienda, name="Tienda"),
    path('agregar/<int:producto_id>/', agregar_producto, name="Add"),
    path('eliminar/<int:producto_id>/', eliminar_producto, name="Del"),
    path('restar/<int:producto_id>/', restar_producto, name="Sub"),
    path('limpiar/', limpiar_carrito, name="CLS"),
    path('detalle_carrito', views.detalle_carrito, name="detalle"),
    path('agregar2/<int:producto_id>/', agregar_producto2, name="Add2"),
    path('checkout/', views.checkout, name="checkout"),
]