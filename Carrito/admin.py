from atexit import register
from django.contrib import admin

from Carrito.models import CarritoModel

# Register your models here.
admin.site.register(CarritoModel)