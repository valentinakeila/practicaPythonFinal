from articulo import *
from datetime import *
from cliente import *
class Paquete:
    def __init__(self, cliente: Cliente) -> None:
        self.__inicio_preparacion = datetime.today().day
        self.__fin_preparacion = None
        self.__paquete_despachado = False
        self.__mis_articulos = []
        self.__cliente = cliente

    @property
    def cliente(self):
        return self.__cliente


    @property
    def inicio_preparacion(self):
        return self.__inicio_preparacion
    
    @property
    def fin_preparacion(self):
        return self.__fin_preparacion
    
    @fin_preparacion.setter
    def fin_preparacion(self, fin):
        self.__fin_preparacion = fin


    @property
    def paquete_despachado(self):
        return self.__paquete_despachado
    
    @paquete_despachado.setter
    def paquete_despachado(self, despachado):
        self.__paquete_despachado = despachado

    @property
    def mis_articulos(self):
        return self.__mis_articulos
    
    @property
    def tiempo_preparacion(self):
        self.__fin_preparacion = datetime.today().day
        tiempoPreparacion = self.__inicio_preparacion - self.__fin_preparacion
        return tiempoPreparacion
    

    @property
    def despachar_paquete(self):
        self.__paquete_despachado = True
        self.__fin_preparacion = datetime.today()

    @property
    def cantidad_articulos_fragiles(self):

        fragiles = 0
        for articulo in self.__mis_articulos:
            if articulo.fragil == True:
                fragiles += 1
        return fragiles
        


    
    def add_articulo(self, articulo:Articulo):
        self.__mis_articulos.append(articulo)

    def remove_articulo(self, articulo:Articulo):
        self.__mis_articulos.remove(articulo)


    def __str__(self) -> str:
        return f" incio {self.__inicio_preparacion} fin {self.__fin_preparacion} duracio{self.tiempo_preparacion} despachado {self.__paquete_despachado} cliente{self.__cliente} fragiles {self.cantidad_articulos_fragiles}"

    

    







