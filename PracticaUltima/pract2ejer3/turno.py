from datetime import *

class Turno:
    def __init__(self, fecha: date, hora: date) -> None:
        self.__fecha = fecha
        self.__hora = hora
        self.__estado = "NO RESERVADO"
        self.__autorizado = False



    @property
    def fecha(self):
        return self.__fecha
    @fecha.setter
    def fecha(self, fecha1):
        self.__fecha = fecha1

    @property
    def hora(self):
        return self.__hora
    @hora.setter
    def hora(self, hora1):
        self.__hora = hora1

    @property
    def estado(self):
        return self.__estado
    @estado.setter
    def estado(self, estado1):
        self.__estado = estado1


    @property
    def autorizado(self):
        return self.__autorizado
    @autorizado.setter
    def autorizado(self, autorizado1):
        self.__autorizado = autorizado1


    def __str__(self) -> str:
        return f"fecha{self.__fecha} hora {self.__hora} estado {self.__estado} autorizado {self.__autorizado}"
    
   