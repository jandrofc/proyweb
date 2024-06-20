from django import forms
from .models import Usuario,Administrador,Cliente,MetodoPago,Pago,Categoria,Producto,Estados,Boleta

from django.forms import ModelForm

from django.contrib.auth.forms import UserCreationForm
from django.contrib.auth.models import User



class RegistroForm(UserCreationForm):
    class Meta:
        model = User
        fields = ['rut','dv','nombre','apellido','correo','telefono','contaseña']


class UsuarioForm(ModelForm):
    class Meta:
        model = Usuario
        fields = ['rut','dv','nombre','apellido','correo','telefono','contaseña']


class AdministradorForm(ModelForm):
    class Meta:
        model = Administrador
        fields = ['activo','fecha_activivacion','fecha_termino','descripcion']

class ClienteForm(ModelForm):
    class Meta:
        model = Cliente
        fields = ['direccion']