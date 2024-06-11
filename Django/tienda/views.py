from django.shortcuts import render

# Create your views here.
from .models import Genero


def index (request):
    Generos= Genero.objects.all()
    context={"generos":Generos}
    return render(request,'index.html',context)



def contactanos (request):
    return render(request,'Paginas/contactanos.html')



def About (request):
    return render(request,'Paginas/Quienes_somos.html')

def Galeria (request):
    return render(request,'Paginas/Galeria.html')
