from titulo import *
class Profesional:
    def __init__(self, nombre: str, apellido: str, nro_documento: str) -> None:
        self.__nombre = nombre
        self.__apellido = apellido
        self.__nro_documento = nro_documento
        self.__mis_titulos = []

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
    def nombre(self, apellido1):
        self.__apellido = apellido1

    @property
    def nro_documento(self):
        return self.__nro_documento
    @nro_documento.setter
    def nro_documento(self, nroDoc):
        self.__nro_documento = nroDoc

    @property
    def mis_titulos(self):
        return self.__mis_titulos
    @mis_titulos.setter
    def mis_titulos(self, titulos):
        self.__mis_titulos = titulos

    def add_titulos(self, titulo: Titulo):
        return self.__mis_titulos.append(titulo)
    
    def remove_titulos(self, titulo: Titulo):
        return self.__mis_titulos.remove(titulo)
    

    def __str__(self) -> str:
        return f"{self.__nombre}{self.__apellido}{self.__nro_documento}"

