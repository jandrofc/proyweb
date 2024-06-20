from django.shortcuts import render
from django.contrib.auth.decorators import login_required

# Create your views here.


#Inicio
def index (request):
    return render(request,'index.html')

#formulario de contacto
def Contactanos (request):
    return render(request,'Paginas/contactanos.html')

#Nosotros
def Nosotros (request):
    return render(request,'Paginas/Quienes_somos.html')
#Galeria de productos
def Galeria (request):
    return render(request,'Paginas/Galeria.html')


#Paginas de cuenta

def Login (request):
    return render(request,'registration/Login.html')

def Registro (request):
    return render(request,'registration/Registro.html')

#boleta
def Boleta (request):
    return render(request,'Paginas/Boleta.html')

#carrito
def Carrito (request):
    return render(request,'Paginas/Carrito.html')



'''
@login_required
def Login (request):
    request.session["usuario"]="admin"
    usuario = request.session["usuario"]
    context = {'usuario':usuario}
    return render(request, 'Login.html', context)
'''
