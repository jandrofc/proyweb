from django.urls import path 
from django.contrib.auth.decorators import login_required

from .views import index,  VerCompras, ListaBoletas,ListaUsuarios, EditarPerfil, eliminarUsuario, Nosotros, Galeria, Contactanos, Login, Registro, Logout, EditarProductos, AñadirProducto, ListaProductos, eliminarProducto, EditarCategoria, AñadirCategoria, ListaCategoria, eliminarCategoria, Tienda_carrito, agregar_producto, eliminar_producto, restar_producto, sumar_producto, limpiar_carrito, Pagina_Boleta

from rest_framework import routers
from .api import ProductoViewSet
routers = routers.DefaultRouter()

routers.register('api/productos', ProductoViewSet, 'productos')

from django.contrib.auth import views as auth_views




urlpatterns = [

    path('', index ,name='index'),
    path('Nosotros', Nosotros ,name='Nosotros'),
    path('Galeria', Galeria ,name='Galeria'),
    path('Contactanos', Contactanos ,name='Contactanos'),
    
    path('Login', Login ,name='Login'),
    path('Registro', Registro ,name='Registro'),
    path('logout', Logout, name='logout'),


    path('EditarPerfil', EditarPerfil, name='EditarPerfil'),
    
    path('ListaUsuarios',ListaUsuarios ,name='ListaUsuarios'),
    path('eliminar_usuario/<id>',eliminarUsuario ,name='eliminarUsuario'),

    path('EditarProducto/<id>',EditarProductos ,name='EditarProducto'),
    path('AñadirProducto',AñadirProducto ,name='AñadirProducto'),
    path('ListaProductos',ListaProductos ,name='ListaProductos'),
    path('eliminar_producto/<id>',eliminarProducto ,name='eliminarProducto'),

    path('EditarCategoria/<id>',EditarCategoria ,name='EditarCategoria'),
    path('AñadirCategoria',AñadirCategoria ,name='AñadirCategoria'),
    path('ListaCategoria',ListaCategoria ,name='ListaCategoria'),
    path('eliminar_categoria/<id>',eliminarCategoria ,name='eliminarCategoria'),

    path('Carrito', Tienda_carrito , name='Carrito'),

    path('ListaBoletas/<id>',ListaBoletas ,name='ListaBoletas'),

    path('VerCompras', VerCompras, name='VerCompras'), 

    path('agregar/<int:id_producto>/', agregar_producto, name='Agregar'),
    path('eliminar/<int:id_producto>/', eliminar_producto, name='eliminar'),
    path('restar/<int:id_producto>/', restar_producto, name='restar'),
    path('sumar/<int:id_producto>/', sumar_producto, name='sumar'),
    path('limpiar/', limpiar_carrito, name='limpiar'),

    path('Boleta/', Pagina_Boleta,name="GenerarBoleta"),


    # reseteo de contraseña
    #1. Se envia un correo con un link para resetear la contraseña
    path('reset_password/', auth_views.PasswordResetView.as_view(template_name = 'recuperarContraseñas/password_reset.html') ,name='password_reset'),
    #2. Se muestra la pagina para resetear la contraseña
    path('reset_password_sent/', auth_views.PasswordResetDoneView.as_view(template_name = 'recuperarContraseñas/intruccionesPassword.html') ,name = 'password_reset_done'),
    #3. Se resetea la contraseña
    path('reset/<uidb64>/<token>/', auth_views.PasswordResetConfirmView.as_view(template_name='recuperarContraseñas/password_form.html') ,name='password_reset_confirm'),
    #4. Se muestra la pagina de confirmación
    path('reset_password_complete/', auth_views.PasswordResetCompleteView.as_view(template_name = 'recuperarContraseñas/password_cambiada.html'), name='password_reset_complete'),




]
urlpatterns += routers.urls  