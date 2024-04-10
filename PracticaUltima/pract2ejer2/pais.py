from datetime import *
from provincia import *
class Pais:
    def __init__(self, nombre: str, codigo:int) -> None:
        self.__nombre = nombre
        self.__codigo = codigo
        self.__fecha_alta = datetime.today()
        self.__mis_provincias =[]

    @property
    def nombre(self):
        return self.__nombre
    
    @nombre.setter
    def nombre(self,nombreValor):
        self.__nombre = nombreValor

    @property
    def codigo(self):
        return self.__codigo
    
    @codigo.setter
    def codigo(self,codigoValor):
        self.__codigo = codigoValor

    @property
    def fecha_alta(self):
        return self.__fecha_alta
    
    @property
    def mis_provincias(self):
        return self.__mis_provincias
    
    @mis_provincias.setter
    def mis_provincias(self, misProvincias):
        self.__mis_provincias = misProvincias

    def add_provincia(self, provincia: Provincia):
        return self.__mis_provincias.append(provincia)
    
    def remove_provincia(self, provincia:Provincia):
        return self.__mis_provincias.remove(provincia)
    
    def __str__(self) -> str:
        return f"nombre{self.__nombre} codigo {self.__codigo} fecha {self.__fecha_alta}"
    
