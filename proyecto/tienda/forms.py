from django import forms
from .models import Usuario,MetodoPago,Pago,Categoria,Producto,Estados,Boleta



from django.contrib.auth.forms import UserCreationForm
from django.contrib.auth.models import User


class RegistroUserForm(UserCreationForm):
    email = forms.EmailField(required=True)  # Asegura que el campo email sea requerido

    class Meta:
        model = User
        fields = ['username', 'first_name', 'last_name', 'email', 'password1', 'password2']

    def clean_email(self):
        email = self.cleaned_data['email']
        if User.objects.filter(email=email).exists():
            raise forms.ValidationError('El correo ya está registrado')
        return email

class PagoForm(forms.ModelForm):
    class Meta:
        model = Pago
        fields = ['id']
        labels = {
            'id': 'Metodo de Pago',
        }
        widgets = {
            'id': forms.Select(attrs={
                'id': 'id',
                'class': 'form-control'}),
        }
        

class UsuarioForm(forms.ModelForm):
    class Meta:
        model = Usuario
        fields = ['rut', 'username', 'nombre', 'apellido', 'correo', 'telefono', 'direccion', 'TipoPago']
        labels = {
            'rut': 'Rut',
            'username': 'Nombre de usuario',
            'nombre': 'Nombre',
            'apellido': 'Apellido',
            'correo': 'Correo',
            'telefono': 'Teléfono',
            'direccion': 'Dirección',
            'TipoPago': 'Tipo de pago',
        }
        widgets = {
            'rut': forms.TextInput(attrs={
                'placeholder':'Ingrese un rut..',
                'id': 'rut',
                'class': 'form-control'}),
            'username': forms.TextInput(attrs={
                'placeholder':'Ingrese un nombre de usuario..',
                'id': 'username',
                'class': 'form-control'}),
            'nombre': forms.TextInput(attrs={
                'placeholder':'Ingrese un nombre..',
                'id': 'nombre',
                'class': 'form-control'}),
            'apellido': forms.TextInput(attrs={
                'placeholder':'Ingrese un apellido..',
                'id': 'apellido',
                'class': 'form-control'}),
            'correo': forms.EmailInput(attrs={
                'placeholder':'Ingrese un correo..',
                'id': 'correo',
                'class': 'form-control'}),
            'telefono': forms.TextInput(attrs={
                'placeholder':'Ingrese un teléfono..',
                'id': 'telefono',
                'class': 'form-control'}),
            'direccion': forms.TextInput(attrs={
                'placeholder':'Ingrese una dirección..',
                'id': 'direccion',
                'class': 'form-control'}),
            'TipoPago': forms.Select(attrs={
                'placeholder':'Ingrese un tipo de pago..',
                'id': 'tipopago',
                'class': 'form-control'}),
        }

class CategoriaForm(forms.ModelForm):
    class Meta:
        model = Categoria
        fields = ['nombre', 'descripcion']
        labels = {
            'nombre': 'Nombre',
            'descripcion': 'Descripción',
        }
        widgets = {
            'nombre': forms.TextInput(attrs={
                'placeholder':'Ingrese un nombre..',
                'id': 'nombre',
                'class': 'form-control'}),
            'descripcion': forms.Textarea(attrs={
                'placeholder':'Ingrese una descripción..',
                'id': 'descripcion',
                'class': 'form-control'}),
        }


class ProductoForm(forms.ModelForm):
    class Meta:
        model = Producto
        fields = ['nombre', 'descripcion', 'imagen', 'precio', 'stock', 'categoria']
        labels = {
            'nombre': 'Nombre',
            'descripcion': 'Descripción',
            'imagen': 'Imagen',
            'precio': 'Precio',
            'stock': 'Stock',
            'categoria': 'Categoría',
        }
        widgets = {
            'nombre': forms.TextInput(attrs={
                'placeholder':'Ingrese un nombre..',
                'id': 'nombre',
                'class': 'form-control'}),
            'descripcion': forms.Textarea(attrs={
                'placeholder':'Ingrese una descripción..',
                'id': 'descripcion',
                'class': 'form-control'}),
            'imagen': forms.FileInput(attrs={
                'id': 'imagen',
                'class': 'form-control'}),
            'precio': forms.NumberInput(attrs={
                'placeholder':'Ingrese un precio..',
                'id': 'precio',
                'class': 'form-control'}),
            'stock': forms.NumberInput(attrs={
                'placeholder':'Ingrese un stock..',
                'id': 'stock',
                'class': 'form-control'}),
            'categoria': forms.Select(attrs={
                'id': 'categoria',
                'class': 'form-control'}),
        }