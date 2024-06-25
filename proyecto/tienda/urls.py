from django.urls import path 
from django.contrib.auth.decorators import login_required

from .views import EditarUsuario, ListaUsuarios, EditarPerfil, eliminarUsuario, index, Nosotros, Galeria, Contactanos, Login, Registro, Logout, EditarProductos, AñadirProducto, ListaProductos, eliminarProducto, EditarCategoria, AñadirCategoria, ListaCategoria, eliminarCategoria, Tienda_carrito, agregar_producto, eliminar_producto, restar_producto, sumar_producto, limpiar_carrito, boleta_boleta



urlpatterns = [
    path('', index ,name='index'),
    path('Nosotros', Nosotros ,name='Nosotros'),
    path('Galeria', Galeria ,name='Galeria'),
    path('Contactanos', Contactanos ,name='Contactanos'),
    
    path('Login', Login ,name='Login'),
    path('Registro', Registro ,name='Registro'),
    path('logout', Logout, name='logout'),
    path('EditarPerfil', EditarPerfil, name='EditarPerfil'),

    path('EditarUsuario/<id>',EditarUsuario ,name='EditarUsuario'),
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

    path('agregar/<int:id_producto>/', agregar_producto, name='Agregar'),
    path('eliminar/<int:id_producto>/', eliminar_producto, name='eliminar'),
    path('restar/<int:id_producto>/', restar_producto, name='restar'),
    path('sumar/<int:id_producto>/', sumar_producto, name='sumar'),
    path('limpiar/', limpiar_carrito, name='limpiar'),
    path('generarBoleta/', boleta_boleta,name="generarBoleta"),

    




]