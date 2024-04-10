from tag import *
from datetime import *
class Video:
    def __init__(self, nombre:str, fecha_publicacion: date) -> None:
        self.__nombre =  nombre
        self.__fecha_publicacion = datetime.today()
        self.__mis_tags = []

    @property
    def nombre(self):
        return self.__nombre
    
    @nombre.setter
    def nombre(self, nombre1):
        self.__nombre = nombre1


    @property
    def fecha_publicacion(self):
        return f"{self.__fecha_publicacion.day}/{self.__fecha_publicacion.month}/{self.__fecha_publicacion.year}"
    
    @property
    def mis_tags(self):
        return self.__mis_tags
    
    def add_tag(self, tag: Tag):
        self.__mis_tags.append(tag)

    def remove_tag(self, tag: Tag):
        self.__mis_tags.remove(tag)

    def __str__(self) -> str:
        return f"nombre{self.__nombre} fecha {self.__fecha_publicacion}"
    



    

    