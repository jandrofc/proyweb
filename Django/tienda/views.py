from django.shortcuts import render
from django.contrib.auth.decorators import login_required

# Create your views here.

def index (request):
    return render(request,'index.html')

def Contactanos (request):
    return render(request,'Paginas/contactanos.html')

def Nosotros (request):
    return render(request,'Paginas/Quienes_somos.html')

def Galeria (request):
    return render(request,'Paginas/Galeria.html')

@login_required
def Login (request):
    request.session["usuario"]="admin"
    usuario = request.session["usuario"]
    context = {'usuario':usuario}
    return render(request, 'Login.html', context)