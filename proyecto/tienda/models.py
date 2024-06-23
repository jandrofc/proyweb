from django.db import models

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
    imagen      = models.ImageField(upload_to='productos', null=True, blank=True)
    precio      = models.IntegerField()
    stock       = models.IntegerField()
    categoria   = models.ForeignKey(Categoria, on_delete=models.CASCADE)

    def __str__(self):
        return self.nombre

    


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
    id_Usuario= models.ForeignKey(Usuario, on_delete=models.CASCADE,default=1)
    productos = models.ManyToManyField(Producto)

    def __str__(self):
        return self.id_boleta

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

    def __str__(self):
        return self.id_detalle

