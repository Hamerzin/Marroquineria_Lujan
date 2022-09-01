from django.urls import path

#cosas para el login
from django.contrib.auth.views import LogoutView
from django.views import View
from productos import views
from productos.views import *

urlpatterns = [
path('administracion', views.administracion, name='administracion'),
path('verprods', views.verproductoss,name="verprods"),
path('buscar', views.buscar, name='buscar'),
path ('busqueda', views.buscarprods, name='busqueda'),
path(r'^borrar/(?P<pk>\d+)$', views.ProductosDelete.as_view(), name='Delete'),
path(r'^(?P<pk>\d+)$', views.ProductoDetalle.as_view(), name='Detalle'),
path(r'^nuevo$', views.ProductosCreacion.as_view(), name='New'),
path(r'^editar/(?P<pk>\d+)$', views.ProductosEditar.as_view(), name='Editar'),
path ('buscar', views.buscarprods, name='busqueda'),
path('buscartipo/', views.buscartipo, name="buscarTipo"),
path('buscartipoliq/', views.buscartipoliq, name="buscarTipoliq"),
path('buscarmochilas/', views.buscarmochilas, name="buscarMochilas"),
path('buscarmarro/', views.buscarmarro, name="buscarMarro"),
]