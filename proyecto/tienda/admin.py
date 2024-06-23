from django.contrib import admin


from .models import Usuario, Pago, Categoria, Producto, Boleta, detalle_boleta, MetodoPago, Estados
# Register your models here.
admin.site.register(Usuario)
admin.site.register(Pago)
admin.site.register(Categoria)
admin.site.register(Producto)
admin.site.register(Boleta)

admin.site.register(detalle_boleta)