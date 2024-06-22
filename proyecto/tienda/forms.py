from django import forms
from .models import Usuario,Administrador,Cliente,MetodoPago,Pago,Categoria,Producto,Estados,Boleta

from django.forms import ModelForm

from django.contrib.auth.forms import UserCreationForm
from django.contrib.auth.models import User



class RegistroForm(UserCreationForm):
    rut = forms.CharField(required=True)
    dv = forms.CharField(required=True)
    nombre = forms.CharField(required=True)
    apellido = forms.CharField(required=True)
    correo = forms.EmailField(required=True)
    telefono = forms.CharField(required=True)
    contraseña = forms.CharField(widget=forms.PasswordInput)
    
    class Meta(UserCreationForm.Meta):
        model = User
        fields = UserCreationForm.Meta.fields

class UsuarioForm(ModelForm):
    class Meta:
        model = Usuario
        fields = ['rut','dv','nombre','apellido','correo','telefono','contraseña']


class AdministradorForm(ModelForm):
    class Meta:
        model = Administrador
        fields = ['activo','fecha_termino','descripcion']

class ClienteForm(ModelForm):
    class Meta:
        model = Cliente
        fields = ['direccion']