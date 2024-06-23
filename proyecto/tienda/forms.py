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