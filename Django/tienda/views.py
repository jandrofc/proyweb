from django.shortcuts import render
from django.contrib.auth.decorators import login_required

#se importan los tipos de formularios que se van a utilizar de forms.py
from .forms import RegistroForm,UsuarioForm,AdministradorForm,ClienteForm


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
    data1 = {
        'form': RegistroForm()
    }
    data2 = {
        'form': UsuarioForm()
    }
    if request.method == 'POST':
        formulario = RegistroForm(request.POST)
        formulario2 = UsuarioForm(request.POST)
        if formulario.is_valid():
            formulario.save()
            formulario2.save()
            data1["mensaje"] = "Usuario registrado"
        else:
            data1["form"] = formulario



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
