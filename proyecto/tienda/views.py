from django.shortcuts import redirect, render
from django.contrib.auth.decorators import login_required
from django.contrib.auth import authenticate, login, logout
from .carrito import Carrito
from tienda.models import Categoria, Producto
#se importan los tipos de formularios que se van a utilizar de forms.py
from .forms import RegistroUserForm, CategoriaForm , ProductoForm

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
def ListaCategoria (request):
    categoria = Categoria.objects.all()
    datos = {
        'categorias':categoria
    }
    return render(request,'Paginas/Administracion/ListaCategorias.html',datos)
def eliminarCategoria(request, id): 
    categoriaEliminada = Categoria.objects.get(id_categoria=id) #similar a select * from... where...
    categoriaEliminada.delete()
    return redirect ('ListaCategoria')

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


def EditarCategoria (request,id):
    ModificarCategoria=Categoria.objects.get(id_categoria=id) #buscamos el objeto
    datos ={
        'form':CategoriaForm(instance=ModificarCategoria)
    }
    if request.method=="POST":
        formulario = CategoriaForm(data=request.POST, instance=ModificarCategoria)
        if formulario.is_valid():
            formulario.save()
            return redirect ('ListaCategoria')
    return render(request, 'Paginas/Administracion/EditarCategoria.html', datos)

def ListaProductos (request):
    productos = Producto.objects.all()
    datos = {
        'Productos':productos
    }
    return render(request,'Paginas/Administracion/ListaProductos.html',datos)

def eliminarProducto(request, id): 
    ProductoEliminado = Producto.objects.get(id_producto=id) #similar a select * from... where...
    ProductoEliminado.delete()
    return redirect ('ListaProductos')


def AñadirProducto (request):
    if request.method == 'POST':
        productoform= ProductoForm(request.POST, request.FILES)
        if productoform.is_valid():
            productoform.save()
            messages.success(request, 'Producto creado exitosamente')
            return redirect('AñadirProducto')
    else:
        productoform = ProductoForm()

    return render(request,'Paginas/Administracion/AñadirProducto.html',{'ProductoForm':productoform})

def EditarProductos (request,id):
    ModificarProducto=Producto.objects.get(id_producto=id) #buscamos el objeto
    datos ={
        'form':ProductoForm(instance=ModificarProducto)
    }
    if request.method=="POST":
        formulario = ProductoForm(data=request.POST, instance=ModificarProducto)
        if formulario.is_valid():
            formulario.save()
            return redirect ('ListaProductos')
    return render(request, 'Paginas/Administracion/EditarProductos.html', datos)




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

