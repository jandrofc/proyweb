from django.shortcuts import render

# Create your views here.

def index (request):
    return render(request,'index.html')


def Contactanos (request):
    return render(request,'Paginas/contactanos.html')



def Nosotros (request):
    return render(request,'Paginas/Quienes_somos.html')

def Galeria (request):
    return render(request,'Paginas/Galeria.html')
