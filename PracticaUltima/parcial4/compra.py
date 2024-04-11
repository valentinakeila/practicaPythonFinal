from datetime import *
from producto import *
from cliente import *
from descuento import *
class Compra:
    def __init__(self, cliente: Cliente) -> None:
        self.__fecha_hora = datetime.today()
        self.__compra_facturada = True
        self.__monto_facturado = 0
        self.__mis_productos = []
        self.__cliente = cliente

    @property
    def cliente(self):
        return self.__cliente


    @property
    def fecha_hora(self):
        return f"{self.__fecha_hora.day} {self.__fecha_hora.month} {self.__fecha_hora.year} {self.__fecha_hora.hour}"
    
    @property
    def compra_facturada(self):
        return self.__compra_facturada
    @compra_facturada.setter
    def compra_facturada(self, compraFacturada):
        self.__compra_facturada = compraFacturada

    @property
    def monto_facturado(self):
        return self.__monto_facturado
    @monto_facturado.setter
    def monto_facturado(self, montoFacturado):
        self.__monto_facturado = montoFacturado

    @property
    def mis_productos(self):
        return self.__mis_productos
    
    def add_producto(self, producto:Producto):
        self.__mis_productos.append(producto)

    def remove_producto(self, producto:Producto):
        self.__mis_productos.remove(producto)


    @property
    def cantidad_productos(self):
        return len(self.__mis_productos)
    
    @property
    def monto_total(self):
        total = 0
        for producto in self.__mis_productos:
            total += producto.precio_unitario
        return total
    
    def facturar_compra(self):
        monto_total = self.monto_total  # Utilizamos el método monto_total para calcular el total

        # Verificar si el cliente tiene número de comunidad
        if self.__cliente.nro_comunidad:
            monto_total = Descuento.pago_con_comunidad(monto_total)
            self.__monto_facturado = monto_total
            self.__compra_facturada = True
        else:
            return f"La compra ya ha sido facturada."
        

    def __str__(self) -> str:
        return f"{self.__cliente}"
        




    


    

    
