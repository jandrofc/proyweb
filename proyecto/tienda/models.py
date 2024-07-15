from django.db import models
from django.contrib.auth.models import User
import datetime 
# Create your models here.


class Categoria(models.Model):
    id_categoria = models.AutoField(primary_key=True,verbose_name="ID")
    nombre       = models.CharField(max_length=20, verbose_name="Nombre")
    descripcion  = models.TextField(max_length=150 ,verbose_name="Descripción")
    def __str__(self):
        return self.nombre


class Producto(models.Model):
    id_producto = models.AutoField(primary_key=True)
    nombre      = models.CharField(max_length=20)
    descripcion = models.TextField(max_length=150)
    imagen      = models.ImageField(upload_to='productos', null=True, blank=True, default='productos/icono.jpeg')
    precio      = models.IntegerField()
    stock       = models.IntegerField()
    categoria   = models.ForeignKey(Categoria, on_delete=models.CASCADE)

    def __str__(self):
        return self.nombre
class Despacho(models.TextChoices):
    DESPACHADO = 'D', 'Despachado'
    NO_DESPACHADO = 'N', 'No Despachado'
    RECIBIDO = 'R', 'Recibido'

class EstadoPago(models.TextChoices):
    PAGADO = 'P', 'Pagado'
    NO_PAGADO = 'N', 'No Pagado'
    PENDIENTE = 'E', 'Pendiente'

    
class Boleta(models.Model):
    id_boleta = models.AutoField(primary_key=True)
    fecha_emitida = models.DateTimeField(blank=True, null=True, default = datetime.datetime.now)
    iva = models.IntegerField()
    total_neto = models.IntegerField()
    total_a_pagar = models.IntegerField()
    estado_pago = models.CharField(max_length=1, choices=EstadoPago.choices, default=EstadoPago.PENDIENTE)
    estado_despacho = models.CharField(max_length=1, choices=Despacho.choices, default=Despacho.NO_DESPACHADO)

    def __str__(self):
        return str(self.id_boleta)



#Es el detalle de una fila de un producto del carro
class DetalleBoleta(models.Model): 
    id_detalle = models.AutoField(primary_key=True)
    id_boleta = models.ForeignKey('Boleta', on_delete=models.CASCADE, related_name='detalles')
    id_producto = models.ForeignKey('Producto', on_delete=models.CASCADE)
    subtotal = models.IntegerField()
    cantidad = models.IntegerField()
    user = models.ForeignKey(User, on_delete=models.CASCADE, related_name='detalles')

    def __str__(self):
        return str(self.id_detalle)