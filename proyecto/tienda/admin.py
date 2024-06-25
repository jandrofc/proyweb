from django.contrib import admin


from .models import Categoria, Producto, Boleta, DetalleBoleta
# Register your models here.
admin.site.register(Categoria)
admin.site.register(Producto)
admin.site.register(Boleta)
admin.site.register(DetalleBoleta)
