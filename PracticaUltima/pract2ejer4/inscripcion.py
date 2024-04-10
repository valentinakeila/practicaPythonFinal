from datetime import *
class Inscripcion:
    prox_num = int(0)
    def __init__(self) -> None:
        self.__nro = Inscripcion.get_nro()
        self.__fecha_hora_inscripcion = datetime.today().hour
        self.__inscripcion_activa = False

    @property
    def nro(self):
        return self.__nro
    
    @property
    def fecha_hora_inscripcion(self):
        return self.__fecha_hora_inscripcion
    
    @fecha_hora_inscripcion.setter
    def fecha_hora_inscripcion(self, fecha):
        self.__fecha_hora_inscripcion = fecha

    @property
    def inscripcion_activa(self):
        return self.__inscripcion_activa
    @inscripcion_activa.setter
    def inscripcion_activa(self, inscripcion):
        self.__inscripcion_activa = inscripcion


    @classmethod
    def get_nro(cls):
        cls.prox_num += 1
        return cls.prox_num
    
    def __str__(self) -> str:
        return f"{self.__nro} {self.__fecha_hora_inscripcion} { self.__inscripcion_activa}"