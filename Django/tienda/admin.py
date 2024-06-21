from django.contrib import admin


from .models import Usuario, Administrador, Cliente, Pago, Categoria, Producto, Boleta, Detalle_compra
# Register your models here.
admin.site.register(Usuario)
admin.site.register(Administrador)
admin.site.register(Cliente)
admin.site.register(Pago)
admin.site.register(Categoria)
admin.site.register(Producto)
admin.site.register(Boleta)
admin.site.register(Detalle_compra)
