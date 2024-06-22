from django.urls import path 
from django.contrib.auth.decorators import login_required

from .views import index,AñadirProducto,EditarCategoria,AñadirCategoria,Logout,Contactanos,Nosotros,Galeria,Login,Registro,Boleta,Carrito,EditarProductos

urlpatterns = [
    path('', index ,name='index'),
    path('Nosotros', Nosotros ,name='Nosotros'),
    path('Galeria', Galeria ,name='Galeria'),
    path('Contactanos', Contactanos ,name='Contactanos'),
    
    path('Login', Login ,name='Login'),
    path('Registro', Registro ,name='Registro'),
    path('logout', Logout, name='logout'),
    
    path('EditarProducto',EditarProductos ,name='EditarProducto'),
    path('AñadirProducto',AñadirProducto ,name='AñadirProducto'),
    path('EditarCategoria',EditarCategoria ,name='EditarCategoria'),
    path('AñadirCategoria',AñadirCategoria ,name='AñadirCategoria'),




    path('Boleta', Boleta ,name='Boleta'),
    path('Carrito', Carrito ,name='Carrito'),


]