from django.shortcuts import redirect, render
from django.contrib.auth.decorators import login_required
from django.contrib.auth import authenticate, login, logout
from .carrito import Carrito
from tienda.models import Categoria, Producto,Boleta, DetalleBoleta
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



#todo lo que esta relacionado con el carrito
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



def Pagina_Boleta (request):
    
    if request.session['carrito'] == {}:
        return redirect('Galeria')
    
    precio_total=0
    IVA=0.19
    for key, value in request.session['carrito'].items():
        precio_total = precio_total + int(value['precio']) * int(value['cantidad'])
    
    total_neto = precio_total*(1-IVA)
    total_iva = round(precio_total*IVA,0)


    #neto es el total de los productos sin iva al consumidor
    #neto mas 19% de iva es el total que el consumidor debe pagar

    EstadoPago = 'E'
    EstadoDespacho = 'N'
    
    boleta = Boleta(iva=total_iva, total_neto=total_neto, total_a_pagar=precio_total, estado_pago=EstadoPago, estado_despacho=EstadoDespacho)
    boleta.save()
    
    productos = []
    for key, value in request.session['carrito'].items():
            producto = Producto.objects.get(id_producto = value['producto_id'])
            cant = value['cantidad']
            subtotal = cant * int(value['precio'])
            detalle = DetalleBoleta(id_boleta = boleta, id_producto = producto, cantidad = cant, subtotal = subtotal)
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