from django.db import models

# Create your models here.
class Usuario(models.Model):
    id_usuario = models.AutoField(primary_key=True)
    rut        = models.CharField(min_length=7, max_length=9,null=False,blank=False)
    dv         = models.CharField(max_length=1,null=False,blank=False)
    nombre     = models.CharField(max_length=20,null=False,blank=False)
    apellido   = models.CharField(max_length=20,null=False,blank=False)
    correo     =  models.EmailField(max_length=20,null=False,blank=False)
    telefono   = models.CharField(min_length=9, max_length=11, null=True,blank=True)

class Administrador(models.Model):
    id_admin = models.AutoField(primary_key=True)
    activo   = models.BooleanField(default=True)
    fecha_activivacion = models.DateTimeField(auto_now_add=True)
    fecha_termino      = models.DateTimeField(auto_now_add=True, null=True, blank=True)
    descripcion        = models.TextField(max_length=150, null=True, blank=True)

class Cliente(models.Model):
    id_cliente = models.AutoField(primary_key=True)
    direccion  = models.CharField(max_length=60)

class Pago(models.Model):
    id = models.TextChoices()
    nombre = models.char
    