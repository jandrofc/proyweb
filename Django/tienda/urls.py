from django.urls import path 
from .views import index,Contactanos,Nosotros,Galeria

urlpatterns = [
    path('Inicio', index ,name='index'),
    path('Nosotros', Nosotros ,name='Nosotros'),
    path('Galeria', Galeria ,name='Galeria'),
    path('Contactanos', Contactanos ,name='Contactanos'),
    
]