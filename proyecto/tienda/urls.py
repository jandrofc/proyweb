from django.urls import path 
from django.contrib.auth.decorators import login_required

from .views import Boleta_detalle, index,Contactanos,Nosotros,Galeria,Login,Registro,Tienda_carrito

urlpatterns = [
    path('', index ,name='index'),
    path('Nosotros', Nosotros ,name='Nosotros'),
    path('Galeria', Galeria ,name='Galeria'),
    path('Contactanos', Contactanos ,name='Contactanos'),
    path('Login', Login ,name='Login'),
    path('Registro', Registro ,name='Registro'),
    
    path('Carrito', Tienda_carrito , name='Carrito'),
]