from django.shortcuts import redirect, render, get_object_or_404
from django.contrib.auth.decorators import login_required, user_passes_test
from django.contrib.auth import authenticate, login, logout
from django.contrib.auth.models import User
from django.contrib.auth.mixins import LoginRequiredMixin
from django.views.generic import UpdateView
from django.urls import reverse_lazy
from .carrito import Carrito
from tienda.models import Categoria, Producto,Boleta, DetalleBoleta
#se importan los tipos de formularios que se van a utilizar de forms.py
from .forms import EditarPerfilForm, RegistroUserForm, CategoriaForm , ProductoForm
from django.db.models import Q
#aletar con mensaje de error o exito en formularios
from django.contrib import messages
from django.core.paginator import Paginator



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
    queryset = request.GET.get("buscar")
    productos = Producto.objects.filter(stock__gt=0)
    if queryset:
        productos = Producto.objects.filter(
            Q(categoria__nombre__iexact=queryset) 
        )
    paginator = Paginator(productos, 12)
    pagina = request.GET.get('page') or 1
    productos = paginator.get_page(pagina)
    pagina_actual = int(pagina)
    paginas = range(1, productos.paginator.num_pages + 1)
    return render(request,'Paginas/Galeria.html',{'productos':productos  ,'paginas':paginas, 'pagina_actual':pagina_actual})


#Paginas de cuenta

def Login (request):
    if request.user.is_authenticated:
        return redirect('index')
    else:
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

def EditarPerfil(request):
    usuario_actual = request.user
    id = request.user.email
    if usuario_actual.is_authenticated and usuario_actual.email == id:
        ModificarUsuario = User.objects.get(email=id)  # Buscamos el objeto
        datos = {
            'form': EditarPerfilForm(instance=ModificarUsuario)
        }
        if request.method == "POST":
            formulario = EditarPerfilForm(data=request.POST, instance=ModificarUsuario, user=usuario_actual)
            if formulario.is_valid():

                formulario.save()
                return redirect('index')
            else:
                messages.error(request, formulario.errors)


                print(formulario.errors)  # Esto imprimirá los errores del formulario en la consola
        return render(request, 'Paginas/Administracion/EditarPerfil.html', datos)
    else:
        # Redirigir o mostrar un mensaje de error si el usuario no está autenticado
        # o si el usuario autenticado no coincide con el perfil que se intenta editar
        return redirect('index')




#Administracion
def check_admin(user):
    return user.groups.filter(name='Admin').exists()

@user_passes_test(check_admin)
def ListaUsuarios (request):
    usuarios = User.objects.all()
    datos = {
        'Usuarios':usuarios
    }
    return render(request,'Paginas/Administracion/ListaUsuarios.html',datos)

@user_passes_test(check_admin)
def eliminarUsuario(request, id):
    usuarioEliminado = User.objects.get(id=id) #similar a select * from... where...
    usuarioEliminado.delete()
    return redirect ('ListaUsuarios')

@user_passes_test(check_admin)
def AñadirUsuario (request):
    if request.method == 'POST':
        usuarioform= EditarPerfilForm(request.POST, request.FILES)
        if usuarioform.is_valid():
            usuarioform.save()
            messages.success(request, 'Usuario creado exitosamente')
            return redirect('AñadirUsuario')
    else:
        usuarioform = EditarPerfilForm()

    return render(request,'Paginas/Administracion/AñadirUsuario.html',{'UsuarioForm':usuarioform})

@user_passes_test(check_admin)
def EditarUsuario (request,id):
    ModificarUsuario=User.objects.get(id=id) #buscamos el objeto
    datos ={
        'form':EditarPerfilForm(instance=ModificarUsuario)
    }
    if request.method=="POST":
        formulario = EditarPerfilForm(data=request.POST, instance=ModificarUsuario)
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

@user_passes_test(check_admin)
def ListaBoletas (request, id):
    usuario = get_object_or_404(User, id=id)
    boletas = Boleta.objects.filter(user=usuario)
    datos = {
        'Boletas': boletas
    }
    return render(request,'Paginas/Administracion/ListaBoletas.html', datos)

def VerCompras(request):
    usuario = request.user
    boletas = Boleta.objects.filter(user=usuario)
    datos = {
        'Boletas': boletas
    }
    return render(request, 'Paginas/Administracion/VerCompras.html', datos)

#todo lo que esta relacionado con el carrito
@login_required(login_url='Login')
def Tienda_carrito (request):
    producto = Producto.objects.all()
    return render(request,'Paginas/Carrito.html',{'productos':producto})

def agregar_producto(request, id_producto):
    carrito = Carrito(request)
    producto = Producto.objects.get(id_producto =id_producto)
    if producto.stock == 0:
        return redirect("Galeria")
    else:
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
def Pagina_Boleta (request):
    

    if request.session['carrito'] == {}:
        return redirect('Galeria')
    

    carrito = Carrito(request)
    for key, value in request.session['carrito'].items():
        producto = Producto.objects.get(id_producto = value['producto_id'])
        producto.stock = producto.stock - value['cantidad']
        producto.save()

    precio_total=0
    IVA=0.19
    for key, value in request.session['carrito'].items():
        precio_total = precio_total + int(value['precio']) * int(value['cantidad'])
    
    total_neto = int(round(precio_total*(1-IVA)))
    total_iva = int(round(precio_total*IVA,0))


    #neto es el total de los productos sin iva al consumidor
    #neto mas 19% de iva es el total que el consumidor debe pagar

    EstadoPago = 'E'
    EstadoDespacho = 'N'

    usuario = request.user
    
    boleta = Boleta(iva=total_iva, total_neto=total_neto, total_a_pagar=precio_total, estado_pago=EstadoPago, estado_despacho=EstadoDespacho)
    boleta.save()
    
    productos = []
    for key, value in request.session['carrito'].items():
            producto = Producto.objects.get(id_producto = value['producto_id'])
            cant = value['cantidad']
            subtotal = cant * int(value['precio'])
            detalle = DetalleBoleta(user=usuario, id_boleta = boleta, id_producto = producto, cantidad = cant, subtotal = subtotal)
            detalle.save()
            productos.append(detalle)
    datos={
        'productos':productos,
        'fecha':boleta.fecha_emitida,
        'iva':boleta.iva,
        'total_neto':boleta.total_neto,
        'total_a_pagar':boleta.total_a_pagar,
        'estado_pago':boleta.estado_pago,
        'estado_despacho':boleta.estado_despacho,
        'id_boleta':boleta.id_boleta,

    }
    #request.session['boleta'] = boleta.id_boleta
    carrito = Carrito(request)
    carrito.limpiar()
    return render(request, 'Paginas/Boleta.html',datos)













"""
def Detalle_Boleta(request):
    
    total_productos = sum([1 for values in request.session["carrito"].values()])
    productos = {}
    precio_total = 0
    IVA=0.19

    #neto es el total de los productos sin iva al consumidor
    #neto mas 19% de iva es el total que el consumidor debe pagar

    for keys, values in request.session["carrito"].items():
        productos={
            values.get('producto_id'): {
                "id_producto" : values.get('producto_id'),
                "nombre": values.get('nombre'),
                "precio": values.get('precio'),
                "categoria": values.get('categoria'),
                "cantidad" : values.get('cantidad'),
                "subtotal": values.get('subtotal')
            }
        }
        precio_total = precio_total + values.get('subtotal', 0)

    precio_bruto = precio_total * (IVA+1) 
    iva = round(precio_bruto * IVA,0)

    total_neto = precio_total
    EstadoPago = 'E'
    EstadoDespacho = 'N'
    Nueva_Boleta=Boleta(iva = iva, total_neto = total_neto, total_a_pagar = precio_bruto, estado_pago = EstadoPago, estado_despacho = EstadoDespacho, productos = productos)
    Nueva_Boleta.save()

    carrito = Carrito(request)
    carrito.limpiar()

   

    return redirect('Mostrar_Boleta', id_boleta=Nueva_Boleta.id_boleta)

def Mostrar_Boleta(request,id_boleta):
    
    Boleta = Boleta.objects.get(id_boleta=id_boleta)

    datos = {
        'boleta': Boleta.id_boleta,
        'fecha': Boleta.fecha_emitida,
        'iva': Boleta.iva,
        'total_neto': Boleta.total_neto,
        'total_a_pagar': Boleta.total_a_pagar,
        'estado_pago': Boleta.estado_pago,
        'estado_despacho': Boleta.estado_despacho,
        'productos': Boleta.productos
    }

    return render(request, 'Pagina_Boleta', datos)
"""