from django.urls import path 
from django.contrib.auth.decorators import login_required

from .views import index,Contactanos,Nosotros,Galeria,Login,Registro,Boleta,Carrito

urlpatterns = [
    path('', index ,name='index'),
    path('Nosotros', Nosotros ,name='Nosotros'),
    path('Galeria', Galeria ,name='Galeria'),
    path('Contactanos', Contactanos ,name='Contactanos'),
    path('Login', Login ,name='Login'),
    path('Registro', Registro ,name='Registro'),
    path('Boleta', Boleta ,name='Boleta'),
    path('Carrito', Carrito ,name='Carrito'),


]