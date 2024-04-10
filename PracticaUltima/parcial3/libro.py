from datetime import *
from genero import *
from autor import *
class Libro:
    def __init__(self, nombre:str,  autor: Autor = None) -> None:
        self.__nombre = nombre
        self.__fecha_publicacion = date.today()
        self.__generos_libro = []
        self.__autor = autor


    @property
    def autor(self):
        return self.__autor
    
    @autor.setter
    def autor(self, autor1):
        self.__autor = autor1


    @property
    def nombre(self):
        return self.__nombre
    
    @nombre.setter
    def nombre(self, nombre1):
        self.__nombre = nombre1

    @property
    def fecha_publicacion(self):
        return f"{self.__fecha_publicacion.day} {self.__fecha_publicacion.month} {self.__fecha_publicacion.year}"
    
    @property
    def generos_libro(self):
        return self.__generos_libros
    
    def add_genero(self, genero:Genero):
        self.__generos_libro.append(genero)

    def  remove_genero(self, genero:Genero):
        self.__generos_libro.remove(genero)


    
    
    def __str__(self) -> str:
        return f"nombre: {self.__nombre}  autor {self.autor.nombre if self.autor else 'unknow'}publicacion: {self.__fecha_publicacion}"
    
    