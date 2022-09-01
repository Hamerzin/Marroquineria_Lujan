from django.urls import path

#cosas para el login
from django.contrib.auth.views import LogoutView
from django.views import View
from appblog import views
from appblog.views import *

urlpatterns = [

path('', views.index, name="index"),
path('index/', views.index, name="index"),
path('login2/', views.login_request, name='login2'),
path('login3/', views.login_request2, name='login3'),
path('register/', views.register, name="register"),
path('logout2/', LogoutView.as_view(template_name='index.html'), name = 'logout2'),
path('editar/',views.editarPerfil, name='editar' ),


]