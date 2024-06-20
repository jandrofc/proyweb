from django.db import models

# Create your models here.
class Usuario(models.Model):
    id_usuario = models.AutoField(primary_key=True)
    rut        = models.CharField(max_length=8,null=False,blank=False)
    dv         = models.CharField(max_length=1,null=False,blank=False)
    nombre     = models.CharField(max_length=20,null=False,blank=False)
    apellido   = models.CharField(max_length=20,null=False,blank=False)
    correo     =  models.EmailField(max_length=20,null=False,blank=False)
    telefono   = models.CharField(max_length=11, null=True,blank=True)

class Administrador(models.Model):
    id_admin = models.AutoField(primary_key=True)
    activo   = models.BooleanField(default=True)
    fecha_activivacion = models.DateTimeField(auto_now_add=True)
    fecha_termino      = models.DateTimeField(auto_now_add=True, null=True, blank=True)
    descripcion        = models.TextField(max_length=150, null=True, blank=True)

class Cliente(models.Model):
    id_cliente = models.AutoField(primary_key=True)
    direccion  = models.CharField(max_length=60)

class MetodoPago(models.TextChoices):
    TRANSFERENCIA = 'T', 'Transferencia'
    TARJETA       = 'C', 'Tarjeta'
    EFECTIVO      = 'E', 'Efectivo'


class Pago(models.Model):
    id = models.CharField(max_length=1,choices=MetodoPago.choices,primary_key=True,)
    nombre = models.CharField(max_length=20)

class Categoria(models.Model):
    id_categoria = models.AutoField(primary_key=True)
    nombre       = models.CharField(max_length=20)
    descripcion  = models.TextField(max_length=150)


class Producto(models.Model):
    id_producto = models.AutoField(primary_key=True)
    nombre      = models.CharField(max_length=20)
    descripcion = models.TextField(max_length=150)
    imagen      = models.ImageField(upload_to='productos', null=True, blank=True)
    precio      = models.IntegerField()
    stock       = models.IntegerField()
    categoria   = models.ForeignKey(Categoria, on_delete=models.CASCADE)
    cantidad_compras = models.IntegerField()


class Estados(models.TextChoices):
    ('P', 'Pendiente'),
    ('E', 'Enviado'),
    ('R', 'Recibido'),
    ('C', 'Cancelado'),

class Boleta(models.Model):
    id_boleta = models.AutoField(primary_key=True)
    fecha_emitida     = models.DateTimeField(auto_now_add=True)
    total     = models.IntegerField()
    neto      = models.IntegerField()
    iva       = models.IntegerField()
    id_estado = models.CharField(max_length=1,choices=Estados.choices)
    id_pago   = models.ForeignKey(Pago, on_delete=models.CASCADE)
    id_cliente= models.ForeignKey(Cliente, on_delete=models.CASCADE)
    productos = models.ManyToManyField(Producto)

class Despacho(models.TextChoices):
    ('D', 'Despachado'),
    ('N', 'No Despachado'),
    ('R', 'Recibido'),
    ('C', 'Cancelado'),

class Detalle_compra(models.Model):
    id_detalle = models.AutoField(primary_key=True)
    fecha_despacho = models.DateTimeField(auto_now_add=True, null=True, blank=True)
    estado_despacho = models.CharField(max_length=1,choices=Despacho.choices)
    fecha_entrega = models.DateTimeField(auto_now_add=True, null=True, blank=True)
    productos = models.ManyToManyField(Producto)
    cantidad   = models.IntegerField()
    precio     = models.IntegerField()
    id_boleta  = models.ForeignKey(Boleta, on_delete=models.CASCADE)

