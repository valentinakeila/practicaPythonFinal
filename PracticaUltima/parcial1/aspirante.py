from titulo import *
class Aspirante:
    def __init__(self,nombre:str ,apellido:str, email:str, num_telefono:str) -> None:
        self.__nombre = nombre
        self.__apellido = apellido
        self.__email = email
        self.__num_telefono = num_telefono
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
    def apellido(self, apellido1):
        self.__apellido = apellido1

    @property
    def email(self):
        return self.__email
    
    @email.setter
    def email(self, email1):
        self.__email = email1

    @property
    def num_telefono(self):
        return self.__num_telefono
    
    @num_telefono.setter
    def num_telefono(self, num_telefono1):
        self.__num_telefono = num_telefono1


    @property
    def mis_titulos(self):
        return self.__mis_titulos
    
    def add_titulo(self, titulo: Titulo):
        self.__mis_titulos.append(titulo)

    def remove_titulo(self, titulo:Titulo):
        self.__mis_titulos.remove(titulo)


    def __str__(self) -> str:
        return f"nombre{self.__nombre} apellido {self.__apellido} email {self.__email} telefono {self.__num_telefono}"


    

    


    



    