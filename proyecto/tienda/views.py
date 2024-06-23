from django.shortcuts import redirect, render
from django.contrib.auth.decorators import login_required
from .carrito import Carrito
from tienda.models import Boleta, Producto,detalle_boleta,Estados
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
    productos= Producto.objects.all()
    return render(request,'Paginas/Galeria.html',{'productos':productos})


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

def Boleta_detalle (request):
    return render(request,'Paginas/Boleta.html')

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
            cant = value['cantidad']
            total_boleta = cant * int(value['precio'])
            detalle = detalle_boleta(cantidad = cant, subtotal = total_boleta, id_boleta = boleta, id_producto = producto)      
            detalle.save()
            productos.append(detalle)
    datos = {
        'boleta': boleta,
        'productos': productos,
        'boleta_total': precio_total,
        'fecha': boleta.fecha_emitida
    }
    request.session['boleta'] = boleta.id_boleta
    carrito = Carrito(request)
    carrito.limpiar()
    return render(request,'Paginas/Boleta.html',datos)

    


'''
@login_required
def Login (request):
    request.session["usuario"]="admin"
    usuario = request.session["usuario"]
    context = {'usuario':usuario}
    return render(request, 'Login.html', context)
'''
