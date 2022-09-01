# PAGINA WEB DE LUJAN MARROQUINERIA
Esta pagina se diseño para un comercio que necesitaba expandirse mediante una Plataforma online, para promocionar sus productos y vender de forma online.

# LINK DE VIDEO DEMO
[![Alt text](https://img.youtube.com/vi/WJmHo-lJy98/1.jpg)](https://www.youtube.com/watch?v=WJmHo-lJy98)

# DOCUMENTACION
Es un proyecto creado mediante PYTHON Framework DJANGO, y utilizando varios templates de BOOTSTRAP para generar la experiencia grafica de usuario.
Se generaron varias aplicaciones CONTACTO SOBRE_NOSOTROS PRODUCTOS y APPBLOG para tener el aplicativo mas ordenado. Se genero la carpeta Static donde se fueron
Gaurdando todo lo referente a los CSS JS y demas archivos que necesita el bootstrap. Tambien se genero la carpeta MEDIA en donde se van a ir cargando
todos los archivos que se suban desde el admin o los formularios creados tanto para los productos como para el avatar

# MODELS.PY
Aca se encuentra el modelo de nuestra base de datos, desde donde luego generare la debida migracion para generar la BD. 
Se crea el model Producto donde se contiene toda la informacion especifica de los productos que el cliente quiere ingresar y manejar.
tambien se crea el model AVATAR para usarlo en la carga de imagen de el usuario

# forms.py
Aqui dentro de las diferentes aplicaciones de el proyecto se encuetran los formularios necesarios para crear la vista en el template y luego volcar los datos en la respectiva
base de datos.

# views.py
En views.py encontramos las diferentes funciones que se crean para darle la funcionalidad a las diferentes necesidades del cliente,
En AppBlog.views se genero todo lo que es el login, el registro y la redireccion a la pagina de inicio.
En Contacto.views se genero todo lo que corresponde con el contacto via Mail, el cual llega mediante MailTrap a un correo electronico.
En Productos.views esta todo lo referente al CRUD ingreso edicion edicion borrado y tambien busqueda de productos.
en Sobre_nosotros.views se genero solo el render para la informacion referente hacia el negocio su historia mision y demas.

# urls.py
Es esta parte se configuran los conjuntos de patrones que Django intentará comparar con la URL recibida para encontrar la vista correcta.

# templates
En esta carpeta dentro de los distintas APPS encontraras los Html que usan las distintas funciones para renderisar sus contenidos.


AUTOR FABIAN DI PAOLO
      dipaolo@gmail.com  
