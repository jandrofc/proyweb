"""
URL configuration for pinponcitos project.

The `urlpatterns` list routes URLs to views. For more information please see:
    https://docs.djangoproject.com/en/5.0/topics/http/urls/
Examples:
Function views
    1. Add an import:  from my_app import views
    2. Add a URL to urlpatterns:  path('', views.home, name='home')
Class-based views
    1. Add an import:  from other_app.views import Home
    2. Add a URL to urlpatterns:  path('', Home.as_view(), name='home')
Including another URLconf
    1. Import the include() function: from django.urls import include, path
    2. Add a URL to urlpatterns:  path('blog/', include('blog.urls'))
"""
from django.contrib import admin
from django.conf import settings
from django.urls import path , include 
from django.conf.urls.static import static
from tienda.views import boleta_boleta, agregar_producto, eliminar_producto, limpiar_carrito, restar_producto, sumar_producto

urlpatterns = [
    path('admin/', admin.site.urls),
    path('',include ('tienda.urls')),
    path('accounts/', include('django.contrib.auth.urls')),
    path('agregar/<int:id_producto>/', agregar_producto, name='Agregar'),
    path('eliminar/<int:id_producto>/', eliminar_producto, name='eliminar'),
    path('restar/<int:id_producto>/', restar_producto, name='restar'),
    path('sumar/<int:id_producto>/', sumar_producto, name='sumar'),
    path('limpiar/', limpiar_carrito, name='limpiar'),
    path('generarBoleta/', boleta_boleta,name="generarBoleta"),
] + static(settings.MEDIA_URL, document_root=settings.MEDIA_ROOT)
