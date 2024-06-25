from django.contrib.auth.models import Group
from django import forms
from .models import Categoria,Producto



from django.contrib.auth.forms import UserCreationForm
from django.contrib.auth.models import User


class RegistroUserForm(UserCreationForm):
    email = forms.EmailField(required=True)  # Asegura que el campo email sea requerido

    class Meta:
        model = User
        fields = ['username', 'first_name', 'last_name', 'email', 'password1', 'password2']
    
    def save(self, commit=True):
        user = super().save(commit=True)
        user.email = self.cleaned_data['email']
        if commit:
            user.save()
            if user.email == "pinponcitos52@gmail.com":
                admin_group, created = Group.objects.get_or_create(name='Admin')
                user.groups.add(admin_group)
        return user
    
class EditarPerfilForm(UserCreationForm):

    class Meta(UserCreationForm.Meta):
        model = User
        fields = ['first_name', 'last_name', 'email', 'password1', 'password2']

    def init(self, args, **kwargs):
        self.user = kwargs.pop('user', None)
        self.email = kwargs.pop('email', None)
        super(EditarPerfilForm, self).init(args, **kwargs)


    def clean_email(self):
        email = self.cleaned_data['email']
        # Filtra excluyendo el correo electrónico del usuario actual si está editando su perfil
        if self.user:
            if User.objects.filter(email=email).exclude(pk=self.user.pk).exists():
                raise forms.ValidationError('El correo ya está registrado MODIFY')
        else:
            if User.objects.filter(email=email).exists():
                raise forms.ValidationError('El correo ya está registrado REGISTER')
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