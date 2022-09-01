from unittest.util import _MAX_LENGTH
from django.db import models

# Create your models here.
class CarritoModel(models.Model):
    codigo=models.IntegerField(max_length=64)
    nombre=models.CharField(max_length=64)
    precio=models.IntegerField()
    tipo=models.CharField(max_length=64)
    

    def __str__(self):
        return f'{self.nombre} -> {self.precio}'

