from django.shortcuts import redirect, render
from django.contrib.auth.decorators import login_required, user_passes_test
from django.contrib.auth import authenticate, login, logout
from .carrito import Carrito
from tienda.models import Categoria, Pago, Producto,Boleta, Usuario,detalle_boleta,Estados
#se importan los tipos de formularios que se van a utilizar de forms.py
from .forms import RegistroUserForm, CategoriaForm , ProductoForm, UsuarioForm

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
    productos= Producto.objects.all()
    return render(request,'Paginas/Galeria.html',{'productos':productos})


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
def check_admin(user):
    return user.groups.filter(name='Admin').exists()

@user_passes_test(check_admin)
def ListaUsuarios (request):
    usuarios = Usuario.objects.all()
    datos = {
        'Usuarios':usuarios
    }
    return render(request,'Paginas/Administracion/ListaUsuarios.html',datos)

@user_passes_test(check_admin)
def eliminarUsuario(request, id):
    usuarioEliminado = Usuario.objects.get(id_usuario=id) #similar a select * from... where...
    usuarioEliminado.delete()
    return redirect ('ListaUsuarios')

@user_passes_test(check_admin)
def AñadirUsuario (request):
    if request.method == 'POST':
        usuarioform= UsuarioForm(request.POST, request.FILES)
        if usuarioform.is_valid():
            usuarioform.save()
            messages.success(request, 'Usuario creado exitosamente')
            return redirect('AñadirUsuario')
    else:
        usuarioform = UsuarioForm()

    return render(request,'Paginas/Administracion/AñadirUsuario.html',{'UsuarioForm':usuarioform})

@user_passes_test(check_admin)
def EditarUsuario (request,id):
    ModificarUsuario=Usuario.objects.get(id_usuario=id) #buscamos el objeto
    datos ={
        'form':UsuarioForm(instance=ModificarUsuario)
    }
    if request.method=="POST":
        formulario = UsuarioForm(data=request.POST, instance=ModificarUsuario)
        if formulario.is_valid():
            formulario.save()
            return redirect ('ListaUsuarios')
    return render(request, 'Paginas/Administracion/EditarUsuario.html', datos)

@user_passes_test(check_admin)
def ListaCategoria (request):
    categoria = Categoria.objects.all()
    datos = {
        'categorias':categoria
    }
    return render(request,'Paginas/Administracion/ListaCategorias.html',datos)

@user_passes_test(check_admin)
def eliminarCategoria(request, id): 
    categoriaEliminada = Categoria.objects.get(id_categoria=id) #similar a select * from... where...
    categoriaEliminada.delete()
    return redirect ('ListaCategoria')

@user_passes_test(check_admin)
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

@user_passes_test(check_admin)
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

@user_passes_test(check_admin)
def ListaProductos (request):
    productos = Producto.objects.all()
    datos = {
        'Productos':productos
    }
    return render(request,'Paginas/Administracion/ListaProductos.html',datos)

@user_passes_test(check_admin)
def eliminarProducto(request, id): 
    ProductoEliminado = Producto.objects.get(id_producto=id) #similar a select * from... where...
    ProductoEliminado.delete()
    return redirect ('ListaProductos')

@user_passes_test(check_admin)
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

@user_passes_test(check_admin)
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



#todo lo que esta relacionado con el carrito
@login_required(login_url='Login')
def Tienda_carrito (request):
    producto = Producto.objects.all()
    return render(request,'Paginas/Carrito.html',{'productos':producto})

def agregar_producto(request, id_producto):
    carrito = Carrito(request)
    producto = Producto.objects.get(id_producto =id_producto)
    carrito.agregar(producto)
    return redirect("Galeria")

def eliminar_producto(request,id_producto):
    carrito = Carrito(request)
    producto = Producto.objects.get( id_producto =id_producto)
    carrito.eliminar(producto)
    return redirect("Carrito")

def sumar_producto(request,id_producto):
    carrito = Carrito(request)
    producto = Producto.objects.get( id_producto =id_producto)
    carrito.agregar(producto)
    return redirect("Carrito")


def restar_producto(request,id_producto):
    carrito = Carrito(request)
    producto = Producto.objects.get( id_producto =id_producto)
    carrito.restar(producto)
    return redirect("Carrito")

def limpiar_carrito(request):
    carrito = Carrito(request)
    carrito.limpiar()
    return redirect("Carrito")
# Generar boleta

@login_required(login_url='Login')
def Boleta_detalle (request):
    return render(request,'Paginas/Boleta.html')

@login_required(login_url='Login')
def boleta_boleta(request):
    precio_total = 0
    for keys, values in request.session["carrito"].items():
        precio = values.get('precio', 0)  # Obtiene el precio o 0 si 'precio' no existe
        cantidad = values.get('cantidad', 1)  # Asume 1 como cantidad predeterminada si no se especifica
        precio_total += precio * cantidad
    boleta = Boleta(total = precio_total)
    boleta.save()
    productos = []
    for key, value in request.session["carrito"].items():
        producto_iid = value.get('producto_id')  # Usa get para evitar KeyError
        if producto_iid is not None:  # Continúa solo si producto_id existe
            producto = Producto.objects.get(id_producto=producto_iid)
            estado_compra= 'Recibido'
            cant = value['cantidad']
            total_boleta = cant * int(value['precio'])
            detalle = detalle_boleta(cantidad = cant, subtotal = total_boleta, id_boleta = boleta, id_producto = producto)      
            detalle.save()
            productos.append(detalle)
    datos = {
        'boleta': boleta,
        'productos': productos,
        'boleta_total': precio_total,
        'fecha': boleta.fecha_emitida,
        'estado': estado_compra
    }
    request.session['boleta'] = boleta.id_boleta
    carrito = Carrito(request)
    carrito.limpiar()
    return render(request,'Paginas/Boleta.html',datos)
