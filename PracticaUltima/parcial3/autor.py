from datetime import *
class Autor:
    def __init__(self, nombre:str,apellido:str,fecha_nacimiento: date) -> None:
        self.__nombre= nombre
        self.__apellido = apellido
        self.__fecha_nacimiento = fecha_nacimiento


    @property
    def nombre(self):
        return self.__nombre
    
    @nombre.setter
    def nombre(self, nombre1):
        self.__nombre = nombre1


    @property
    def apellido(self):
        return self.__apellido
    
    @apellido.setter
    def apellido(self, apellido1):
        self.__apellido = apellido1


    
    @property
    def fecha_nacimiento(self):
        return self.__apellido
    
    @fecha_nacimiento.setter
    def fecha_nacimiento(self, fecha_nacimiento1):
        self.__fecha_nacimiento = fecha_nacimiento1


    def __str__(self) -> str:
        return f"nombre: {self.__nombre} apellido {self.__apellido} nacimiento: {self.__fecha_nacimiento}"

    