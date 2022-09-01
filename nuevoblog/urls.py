"""nuevoblog URL Configuration

The `urlpatterns` list routes URLs to views. For more information please see:
    https://docs.djangoproject.com/en/4.0/topics/http/urls/
Examples:
Function views
    1. Add an import:  from my_app import views
    2. Add a URL to urlpatterns:  path('', views.home, name='home')
Class-based views
    1. Add an import:  from other_app.views import Home
    2. Add a URL to urlpatterns:  path('', Home.as_view(), name='home')
Including another URLconf
    1. Import the include() function: from django.urls import include, path
    2. Add a URL to urlpatterns:  path('blog/', include('blog.urls'))
"""
from django.conf import settings
from django.contrib import admin
from django.urls import path, include, re_path
from django.conf.urls.static import static
from django.views.static import serve
from django.conf.urls import handler404
from appblog.views import Error404view
from messenger.urls import messenger_patterns
from profiles.urls import profiles_patterns





urlpatterns = [
    path('admin/', admin.site.urls),
    path('', include('appblog.urls')),
    path('contacto/', include('contacto.urls')),
    path('sobre_nosotros/', include('sobre_nosotros.urls')),
    path('productos/', include('productos.urls')),
    path('carrito/', include('Carrito.urls')), 
    path('pages/', include('pages.urls')),
    path('accounts/',include('django.contrib.auth.urls')),
    path('accounts/',include('registration.urls')),
    path('messenger/', include(messenger_patterns)),
    path('profiles/', include(profiles_patterns)),
    path('procesar/',include('pedidos.urls')),
    re_path(r'^media/(?P<path>.*)$', serve,{'document_root': settings.MEDIA_ROOT}),

    re_path(r'^static/(?P<path>.*)$', serve,{'document_root': settings.STATIC_ROOT}),

]


handler404= Error404view.as_view()





