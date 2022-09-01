from django.urls import path
from . import views

urlpatterns = [
    path('', views.sobrenos, name="nosotros"),
]