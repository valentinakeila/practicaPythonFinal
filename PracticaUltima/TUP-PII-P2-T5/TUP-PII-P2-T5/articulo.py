from cod_generator import *

class Articulo:
    codigos_utilizados = set()
    def __init__(self, descripcion:str, fragil= None) -> None:
        self.__descripcion = descripcion
        self.__codigo =self.generar_y_agregar_codigo_utilizado()
        self.__fragil = fragil

    @property
    def descripcion(self):
        return self.__descripcion
    
    @property
    def codigo(self):
        return self.__codigo
    
    @property
    def fragil(self):
        return self.__fragil
    
    @fragil.setter
    def fragil(self, fragil1):
        self.__fragil = fragil1


    @staticmethod
    def generar_y_agregar_codigo_utilizado():
        codigo = CodGenerator.generar_codigo()
        Articulo.codigos_utilizados.add(codigo)
        return codigo
        
    
    def __str__(self) -> str:
        return f" descripcion{ self.__descripcion} codigo {self.__codigo} fragil {self.__fragil}"
    

