from django.shortcuts import render
from django.contrib.auth.decorators import login_required
from django.contrib import messages
from Carrito.Carrito import Carrito
from .models import Pedido, lineapedido
from django.shortcuts import redirect
from django.template.loader import render_to_string
from django.utils.html import strip_tags
from django.core.mail import send_mail
from Carrito.context_processor import total_carrito
from pedidos.models import ShippingAddress

@login_required(login_url="login2")

def procesar_pedido(request):
    pedido=Pedido.objects.create(user=request.user)
    carrito=Carrito(request)
    lineas_pedido=list()
    total=total_carrito(request)
    for key, value in carrito.carrito.items():
        
        lineas_pedido.append(lineapedido(
            producto_id=key,
            cantidad=value["cantidad"],
            user=request.user,
            pedido=pedido,
            imagen=value["imagen"],
            precio=value["precio"],
            nombre=value["nombre"]
                        
                         ))
        

    lineapedido.objects.bulk_create(lineas_pedido)
    shipping=list()
    
    ShippingAddress.objects.create(
		customer=request.user,
		order=pedido,
		address=request.GET.get('address'),
		city=request.GET.get('city'),
		state=request.GET.get('state'),
		zipcode=request.GET.get('zipcode'),
        telefono=request.GET.get('telefono'),
        country=request.GET.get('country')
		)
   
    shipping=ShippingAddress.objects.filter(order_id=pedido)
    
    print(shipping)
    
    if (request.user.profile.first_name):
        nombres=request.user.profile.first_name
    else:
        nombres="no ingresado"
    
    if (request.user.profile.last_name):     
        apellidos=request.user.profile.last_name
    else:
        apellidos="no ingresado"

    enviar_mail(
       pedido=pedido,
       lineas_pedido=lineas_pedido,
        nombreusuario=request.user.username,
        email=request.user.email,
        cantidad=["cantidad"],
        total=total_carrito(request),
        shipping=shipping,
        nombre=nombres,
        apellido=apellidos
       
    )
    messages.success(request, "El pedido se creo correctamente")
    contexto="SU COMPRA A SIDO VALIDADA NOS PONDREMOS EN CONTACTO CON USTED EN UNOS MOMENTOS PARA FINALIZAR LA TRANSACCION"
   
    Carrito.limpiar(request)
    return render(request,"exito.html", {"contexto":contexto})
    
    

def enviar_mail(**kwargs):
    asunto="Gracias por tu pedido en Lujan Marroquineria"
    mensaje=render_to_string("emails/pedido.html", {
        "pedido": kwargs.get("pedido"),
        
        "lineas_pedido": kwargs.get("lineas_pedido"),
        "nombreusuario":kwargs.get("nombreusuario"),
        "email": kwargs.get("email"),
        "total":kwargs.get("total"),
        "shipping":kwargs.get("shipping")
        }
    )
    asunto2="Hola Nati recibiste un pedido desde la Pagina WEB estos son los datos"
    
    mensaje2=render_to_string("emails/pedido2.html", {
        "pedido": kwargs.get("pedido"),
        "lineas_pedido": kwargs.get("lineas_pedido"),
        "nombreusuario":kwargs.get("nombreusuario"),
        "email": kwargs.get("email"),
        "total":kwargs.get("total"),
        "shipping":kwargs.get("shipping"),
        "nombre":kwargs.get("nombre"),
        "apellido":kwargs.get("apellido")}
    )

    mensaje_texto=strip_tags(mensaje)
    mensaje_texto2=strip_tags(mensaje2)
    from_email="lujan@lujanmarroquineria.tk"
    to=kwargs.get("email")
    cc_email="natalibirri@gmail.com"
    send_mail(asunto, mensaje_texto, from_email, [to], html_message=mensaje)
    send_mail(asunto2, mensaje_texto2, from_email, [cc_email], html_message=mensaje2)