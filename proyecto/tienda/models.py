from django.db import models
import datetime 
# Create your models here.


class MetodoPago(models.TextChoices):
    TRANSFERENCIA = 'T', 'Transferencia'
    TARJETA       = 'C', 'Tarjeta'
    EFECTIVO      = 'E', 'Efectivo'

#crear esos 3 valores inmediatamente

class Pago(models.Model):
    id = models.CharField(max_length=1,choices=MetodoPago.choices,primary_key=True,)
    nombre = models.CharField(max_length=20)
    def __str__(self):
        return self.nombre

class Usuario(models.Model):
    id_usuario = models.AutoField(primary_key=True)
    rut        = models.CharField(max_length=8,null=True,blank=True)
    username   = models.CharField(max_length=20,default='usuario')
    nombre     = models.CharField(max_length=20)
    apellido   = models.CharField(max_length=20)
    correo     =  models.EmailField(max_length=20)
    telefono   = models.CharField(max_length=11, null=True,blank=True)
    direccion  = models.CharField(max_length=60,null=True,blank=True)
    TipoPago  = models.ForeignKey(Pago, on_delete=models.CASCADE ,null=True,blank=True)


    def __str__(self):
        return self.username





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

    
class Boleta(models.Model):
    id_boleta = models.AutoField(primary_key=True)
    fecha_emitida = models.DateTimeField(blank=True, null=True, default = datetime.datetime.now)
    total     = models.IntegerField()
    
    def __str__(self):
        return str(self.id_boleta)

class Despacho(models.TextChoices):
    DESPACHADO = 'D', 'Despachado'
    NO_DESPACHADO = 'N', 'No Despachado'
    RECIBIDO = 'R', 'Recibido'
    CANCELADO = 'C', 'Cancelado'

class EstadoPago(models.TextChoices):
    PAGADO = 'P', 'Pagado'
    NO_PAGADO = 'N', 'No Pagado'
    PENDIENTE = 'E', 'Pendiente'

class DetalleBoleta(models.Model):
    id_detalle = models.AutoField(primary_key=True)
    boleta = models.ForeignKey(Boleta, on_delete=models.CASCADE, related_name='detalles')
    cantidad = models.IntegerField()
    iva = models.IntegerField()
    total_neto = models.IntegerField()
    total_a_pagar = models.IntegerField()
    estado_pago = models.CharField(max_length=1, choices=EstadoPago.choices, default=EstadoPago.PENDIENTE)
    estado_despacho = models.CharField(max_length=1, choices=Despacho.choices, default=Despacho.NO_DESPACHADO)
    productos = models.JSONField()

    def __str__(self):
        return f"Detalle {self.id_detalle} de Boleta {self.boleta.id_boleta}"