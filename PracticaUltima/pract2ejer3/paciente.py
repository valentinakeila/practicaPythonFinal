from datetime import *


class Paciente:
    def __init__(self, nombre_apellido: str, nro_documento: str, direccion: str, fecha_nacimiento:date):
        self.__nombre_apellido = nombre_apellido
        self.__nro_documento = nro_documento
        self.__direccion = direccion
        self.__fecha_nacimiento = fecha_nacimiento

    @property
    def nombre_apellido(self):
        return self.__nombre_apellido
    
    @nombre_apellido.setter
    def nombre_apellido(self, nombreApellido):
        self.__nombre_apellido = nombreApellido

    @property
    def nro_documento(self):
        return self.__nro_documento
    
    @nro_documento.setter
    def nro_documento(self, nroDocumento):
        self.__nro_documento = nroDocumento

    @property
    def direccion(self):
        return self.__direccion
    
    @direccion.setter
    def direccion(self, diraccion1):
        self.__direccion = diraccion1

    @property
    def fecha_nacimiento(self):
        return self.__fecha_nacimiento
    
    @fecha_nacimiento.setter
    def fecha_nacimiento(self, fechaNacimiento):
        self.__fecha_nacimiento = fechaNacimiento

    @property
    def edad(self) -> int:
        today = date.today()
        edad = today.year - self.__fecha_nacimiento - ((today.month, today.day) < (self.__fecha_nacimiento.month, self.__fecha_nacimiento.day))
        return edad
    
    """
    @property
    def edad(self) -> int:
        return relativedelta(date.today(), self.__fecha_nacimiento).years
    """

    def __str__(self) -> str:
        return f"nombre {self.__nombre_apellido}documento {self.__nro_documento}direccion{self.__direccion} nacimiento{self.__fecha_nacimiento}"
    

    