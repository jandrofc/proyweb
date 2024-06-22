from django.shortcuts import redirect, render
from django.contrib.auth.decorators import login_required
from django.contrib.auth import authenticate, login, logout
from .carrito import Carrito
from tienda.models import Categoria, Producto
#se importan los tipos de formularios que se van a utilizar de forms.py
from .forms import RegistroUserForm, CategoriaForm

#aletar con mensaje de error o exito en formularios
from django.contrib import messages



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
    if request.method == 'POST':
        correo = request.POST.get('correo')
        password = request.POST.get('password')

        usuario = authenticate(request, username=correo, password=password)

        if usuario is not None:
            login(request, usuario)
            return redirect('index')
        else:
            
            messages.info(request, 'Correo o contraseña incorrecta')
            
    
    context = {}
    return render(request,'registration/Login.html')

def Registro (request):
    form = RegistroUserForm()
    if request.method == 'POST' or None:
        form = RegistroUserForm(request.POST)
        if form.is_valid():
            form.save()

            messages.success(request, 'Cuenta creada exitosamente')

            return redirect('Login')
    context = {'form':form}
    return render(request, 'registration/registro.html',context)

def Logout (request):
    logout(request) #cierra la sesion funcion de django
    return redirect('index')

#Administracion

def EditarProductos (request):
    return render(request,'Paginas/Administracion/EditarProductos.html')

def AñadirProducto (request):
    return render(request,'Paginas/Administracion/AñadirProducto.html')

def EditarCategoria (request):
    return render(request,'Paginas/Administracion/EditarCategoria.html')

def AñadirCategoria (request):
    if request.method == 'POST':
        categoriaform= CategoriaForm(request.POST, request.FILES)
        if categoriaform.is_valid():
            categoriaform.save()
            messages.success(request, 'Categoria creada exitosamente')
            return redirect('AñadirCategoria')
    else:
        categoriaform = CategoriaForm()

    return render(request,'Paginas/Administracion/AñadirCategoria.html',{'CategoriaForm':categoriaform})


#boleta
@login_required(login_url='Login')
def Boleta (request):
    return render(request,'Paginas/Boleta.html')

#todo lo que esta relacionado con el carrito
@login_required(login_url='Login')
def tienda_carrito (request):
    producto = producto.objects.all()
    return render(request,'Paginas/Carrito.html',{'productos':Producto})

def agragar_producto(request,id_producto):
    carrito = Carrito(request)
    producto = Producto.objects.get(id =id_producto)
    carrito.agregar(producto)
    return redirect("tienda:tienda")

def eliminar_producto(request,id_producto):
    carrito = Carrito(request)
    producto = Producto.objects.get(id=id_producto)
    carrito.eliminar(producto)
    return redirect("tienda:tienda")

def restar_producto(request,id_producto):
    carrito = Carrito(request)
    producto = Producto.objects.get(id=id_producto)
    carrito.restar(producto)
    return redirect("tienda:tienda")

def limpiar_carrito(request):
    carrito = Carrito(request)
    carrito.limpiar()
    return redirect("tienda:tienda")
# mostrar en galeria
def galeria(request):
    productos = Producto.objects.all()  # Obtiene todos los productos
    categorias = Categoria.objects.all()  # Obtiene todas las categorías
    return render(request, 'Galeria.html', {'Producto': productos, 'categorias': categorias})

