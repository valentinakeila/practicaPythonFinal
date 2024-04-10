from titulo import *
from datetime import *

class Carrera:
    def __init__(self, nombre:str, comienzo:date) -> None:
        self.__nombre = nombre
        self.__comienzo = comienzo
        self.__titulos_grado_requeridos = []


    @property
    def nombre(self):
        return self.__nombre
    
    @nombre.setter
    def nombre(self, nombre1):
        self.__nombre = nombre1

    @property
    def comienzo(self):
        return self.__comienzo
    
    @comienzo.setter
    def comienzo(self, comienzo1):
        self.__comienzo = comienzo1

    @property
    def titulos_grado_requeridos(self):
        return self.__titulos_grado_requeridos
    
    def add_titulo_requerido(self, titulo: Titulo):
        self.__titulos_grado_requeridos.append(titulo)

    def remove_titulo_requerido(self, titulo:Titulo):
        self.__titulos_grado_requeridos.remove(titulo)

    @property
    def cantidad_titulos_requeridos(self):
        return len(self.__titulos_grado_requeridos)
    
    def __str__(self) -> str:
        return f"nombre{self.__nombre} comienzo {self.__comienzo} titulos requeridos {self.cantidad_titulos_requeridos}"
    



    


    


    