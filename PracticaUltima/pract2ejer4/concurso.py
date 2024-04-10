from inscripcion import *
from datetime import *
from titulo import *
class Concurso:
    def __init__(self, nombre: str, fecha_inscripcion_desde: date, fecha_inscripcion_hasta: date) -> None:
        self.__nombre = nombre
        self.__fecha_inscripcion_desde = fecha_inscripcion_desde
        self.__fecha_inscripcion_hasta = fecha_inscripcion_hasta
        self.__mis_incripciones = []
        self.__titulos_grado_requerido = []

    @property
    def nombre(self):
        return self.__nombre
    @nombre.setter
    def nombre(self, nombre1):
        self.__nombre = nombre1

    @property
    def fecha_inscripcion_desde(self):
        return self.__fecha_inscripcion_desde
    @fecha_inscripcion_desde.setter
    def fecha_inscripcion_desde(self, fecha_inscripcion_desde1):
        self.__fecha_inscripcion_desde = fecha_inscripcion_desde1

    @property
    def fecha_inscripcion_hasta(self):
        return self.__fecha_inscripcion_hasta
    @fecha_inscripcion_hasta.setter
    def fecha_inscripcion_hasta(self, fecha_inscripcion_hasta1):
        self.__fecha_inscripcion_hasta = fecha_inscripcion_hasta1

    @property
    def mis_incripciones(self):
        return self.__mis_incripciones
    @mis_incripciones.setter
    def mis_incripciones(self, mis_incripciones1):
        self.__mis_incripciones = mis_incripciones1

    def add_inscripcion(self, inscripcion: Inscripcion):
        return self.__mis_incripciones.append(inscripcion)
    
    def remove_inscripcion(self, inscripcion:Inscripcion):
        return self.__mis_incripciones.remove(inscripcion)
    @property
    def titulos_grado_requerido(self) -> list:
        return self.__titulos_grado_requerido
    
    def add_titulo_requerido(self, titulo: Titulo) -> None:
        self.__titulos_grado_requerido.append(titulo)

    def remove_titulo_requerido(self, titulo: Titulo) -> None:
        self.__titulos_grado_requerido.remove(titulo)

    def __str__(self) -> str:
        return f" {self.__nombre}{self.__fecha_inscripcion_desde} {self.__fecha_inscripcion_hasta}"
    
    def get_inscripciones_activas():
        
