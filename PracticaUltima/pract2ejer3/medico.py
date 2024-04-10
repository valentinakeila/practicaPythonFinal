from especialidad import *
from datetime import *

class Medico:
    def __init__(self, nombre_apellido: str, matricula: str, fecha_matricula: date):
        self.__nombre_apellido = nombre_apellido
        self.__matricula = matricula
        self.__fecha_matricula = fecha_matricula
        self.__mis_especialidades = []


    @property
    def nombre_apellido(self):
        return self.__nombre_apellido
    
    @nombre_apellido.setter
    def nombre_apellido(self, nombreApellido):
        self.__nombre_apellido = nombreApellido

    @property
    def matricula(self):
        return self.__matricula
    
    @matricula.setter
    def matricula(self, matricula1):
        self.__matricula = matricula1

    @property
    def fecha_matricula(self):
        return self.__fecha_matricula
    
    @fecha_matricula.setter
    def fecha_matricula(self, fechaMatricula):
        self.__fecha_matricula = fechaMatricula


    @property
    def mis_especialidades(self):
        return self.__mis_especialidades
    
    @mis_especialidades.setter
    def mis_especialidades(self, misEspecialidades):
        self.__mis_especialidades = misEspecialidades

    
    def add_especialidad(self, especialidad:Especialidad ):
         return self.__mis_especialidades.append(especialidad)
    
    def remove_especialidad(self, especialidad: Especialidad):
        return self.__mis_especialidades.remove(especialidad)
    

    def __str__(self) -> str:
        return f"nombre {self.__nombre_apellido} matricula {self.__matricula}fecha matricula{self.__fecha_matricula}"
    
    