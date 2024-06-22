from django import forms
from .models import Usuario,Administrador,Cliente,MetodoPago,Pago,Categoria,Producto,Estados,Boleta



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
            'nombre': forms.TextInput(attrs={'class': 'form-control'}),
            'descripcion': forms.Textarea(attrs={'class': 'form-control'}),
        }