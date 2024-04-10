from aspirante import *
from carrera import *
from datetime import *

class Inscripcion:
    prox_nro =int(0)
    def __init__(self, aspirante: Aspirante, carrera:Carrera) -> None:
        self.__aspirante = aspirante
        self.__carrera = carrera
        self.__nro = Inscripcion.get_prox_nro()
        self.__fecha_inscripcion = datetime.today()
        self.__inscripcion_activa = True

    @property
    def aspirante(self):
        return self.__aspirante
    
    @aspirante.setter
    def aspirante(self, aspirante1):
        self.__aspirante = aspirante1

    @property
    def carrera(self):
        return self.__carrera
    
    @carrera.setter
    def carrera(self, carrera1):
        self.__carrera = carrera1

    @property
    def nro(self):
        return self.__nro
    
    @property
    def fecha_inscripcion(self):
        return self.__fecha_inscripcion
    
    @property
    def inscripcion_activa(self) -> bool:
        return self.__inscripcion_activa

    @inscripcion_activa.setter
    def inscripcion_activa(self, nuevo_estado:bool) -> None:
        self.__inscripcion_activa = nuevo_estado
    

    @classmethod
    def get_prox_nro(cls):
        cls.prox_nro += 1
        return cls.prox_nro
    
    def __str__(self) -> str:
        return f"aspirante {self.__aspirante} carrera {self.__carrera} nro {self.__nro} fecha{self.__fecha_inscripcion} activa {self.__inscripcion_activa} "

    
