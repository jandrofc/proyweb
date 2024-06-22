from django import forms
from .models import Usuario,Administrador,Cliente,MetodoPago,Pago,Categoria,Producto,Estados,Boleta



from django.contrib.auth.forms import UserCreationForm
from django.contrib.auth.models import User


class RegistroUserForm(UserCreationForm):
    class Meta:
        model = User
        fields = [ 'username', 'first_name', 'last_name', 'email', 'password1', 'password2']

