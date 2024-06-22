class Carrito:
    def __init__(self,request):
        self.request = request
        self.session = request.session
        carrito = self.session["carrito"]
        if not carrito:
            self.session["carrito"] = {}
            self.carrito = self.session["carrito"]
        else:
            self.carrito = carrito
    
    def agregar(self,Producto):
        id = str(Producto.id)
        if id not in self.carrito.Keys():
            self.carrito[id]={
                "producto_id" : Producto.id,
                "nombre": Producto.nombre,
                "imagen": Producto.imagen,
                "precio" : Producto.precio,
                "stock" : Producto.stock,
                "categoria": Producto.categoria,
                "cantidad" : 1,
            }
        else: 
            self.carrito[id]["cantidad"] +=1
            self.carrito[id]["precio"] += Producto.precio
        self.guardar_carrito()
    
    def guardar_carrito(self):
        self.session["carrito"] = self.carrito
        self.session.modified = True

    def eliminar(self,Producto):
        id = str(Producto.id)
        if id in self.carrito:
            del self.carrito[id]
            self.guardar_carrito()
    def restar(self,Producto):
        id = str(Producto.id)
        if id  in self.carrito.Keys():
            self.carrito[id]["cantidad"] -= 1
            self.carrito[id]["precio"] -= Producto.precio
            if self.carrito[id]["cantidad"] <= 0: self.eliminar(Producto)
            self.guardar_carrito()
    
    def limpiar(self):
        self.carrito["carrito"] = {}
        self.session.modified = True
        