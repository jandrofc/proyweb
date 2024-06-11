from django.shortcuts import render

# Create your views here.

def index (request):
    return render(request,'index.html')


def contactanos (request):
    return render(request,'Paginas/contactanos.html')



def About (request):
    return render(request,'Paginas/Quienes_somos.html')

def Galeria (request):
    return render(request,'Paginas/Galeria.html')
