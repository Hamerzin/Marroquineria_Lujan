from itertools import product
from nturl2path import url2pathname
from profile import Profile
import profile
from django.http import HttpResponseRedirect, JsonResponse
from django.shortcuts import redirect, render, HttpResponse
from django.urls import reverse_lazy
from django.views.generic import ListView, TemplateView
from django.views.generic.detail import DetailView
from django.views.generic.edit import CreateView, UpdateView, DeleteView
from Carrito import urls
from appblog import models
from appblog.models import *
from django.contrib.auth.forms import AuthenticationForm
from django.contrib.auth import login, logout, authenticate
from django.contrib.auth.forms import AuthenticationForm, UserCreationForm
from django.contrib.auth.mixins import LoginRequiredMixin
from django.contrib.auth.decorators import login_required
from appblog.forms import *
import smtplib
from django.template import RequestContext
from django.shortcuts import HttpResponseRedirect


class Error404view(TemplateView):
      template_name="404.html"



#----------------LOGIN----------------------------------------------
def login_request(request):
    
      if request.method == "POST":
          
            form = AuthenticationForm(request, data = request.POST)
            
            if form.is_valid():
                  usuario = form.cleaned_data.get('username')
                  contra = form.cleaned_data.get('password')

                  user = authenticate(username = usuario , password = contra)
                  print(1)
                  if user is not None:
                        login(request, user)

                        return redirect("profile")
                  else:
                        print(2)
                        return render (request, "index.html", {"mensaje":"Error en los datos"})
            else:
                  return render(request, "login2.html", {'form': form,"mensaje":"Formulario erroneo"})
      
      form = AuthenticationForm()
      print(3)
      return render(request, "login2.html", {'form': form})

def login_request2(request):
    
      if request.method == "POST":
          
            form = AuthenticationForm(request, data = request.POST)
            
            if form.is_valid():
                  usuario = form.cleaned_data.get('username')
                  contra = form.cleaned_data.get('password')

                  user = authenticate(username = usuario , password = contra)
                  print(1)
                  if user is not None:
                        login(request, user)

                        return redirect("profile")
                  else:
                        print(2)
                        return render (request, "index.html", {"mensaje":"Error en los datos"})
            else:
                  return render(request, "login2.html", {'form': form,"mensaje":"Formulario erroneo"})
      
      form = AuthenticationForm()
      print(3)
      return render(request, "login3.html", {'form': form})
#--------------------------------------------------------------------------

#-------------------REGISTRO-----------------------------------------------
def register(request):
      
      if request.method == "POST":

            form = UserRegisterForm(request.POST)

            if form.is_valid():
                  username = form.cleaned_data['username']
                 
                  form.save()

                  return redirect("login3")
      else: 
            form = UserRegisterForm()

      return render(request, "registro.html", {"form": form})


#-------------------------EDICION DE PERFIL-------------------------------------------------
@login_required
def editarPerfil(request):
      #se instancia el Login; 
      usuario = request.user
      
      if request.method == 'POST':
            miFormulario = UserEditForm(request.POST)
            if miFormulario.is_valid(): #si pasa la validación Django
                  informacion = miFormulario.cleaned_data
                  
                  #datos que modificaríamos
                  usuario.email = informacion['email']#alg@algo.com
                  usuario.password1 = informacion['password1']#pass
                  usuario.password2 = informacion['password2']
                  usuario.last_name = informacion['last_name']
                  usuario.first_name = informacion['first_name']
                  
                  usuario.save()
            
                  return render(request, "inicio.html") #vuelvo a inicio

      else:
            #creo el formulario con los datos que voy a modificar
            miFormulario = UserEditForm(initial={'email':usuario.email,'last_name':usuario.last_name,'first_name':usuario.first_name})
          
      #voy al HTML que me permite editar
      return render(request, "editarperfil.html", {"miFormulario": miFormulario, "usuario": usuario})


#----------------------------PAGINA DE INICIO----------------------------------------------

def index(request):
      return render(request, "index.html")



