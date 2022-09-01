from django.contrib import admin
from .models import  Productos
# Register your models here.



class prod(admin.ModelAdmin):
    
    list_display = ('tipo', 'nombre', 'precio', 'imagen')
    ordering = ('nombre', 'precio')
    search_fields = ('tipo','nombre')

admin.site.register(Productos, prod)

