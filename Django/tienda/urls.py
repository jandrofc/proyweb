from django.urls import path 
from .views import index,contactanos,About,Galeria

urlpatterns = [
    path('index', index ,name='index'),
    path('About', About ,name='About'),
    path('Galeria', Galeria ,name='Galeria'),
    path('contactanos', contactanos ,name='contactanos'),
]