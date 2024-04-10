from datetime import *
class Localidad:
    def __init__(self, nombre: str, codigo:int, cod_postal: int) -> None:
        self.__nombre  = nombre
        self.__codigo = codigo
        self.__cod_postal = cod_postal
        self.__fecha_alta = datetime.today()

    @property
    def nombre(self):
        return self.__nombre
    
    @nombre.setter
    def nombre(self,nombreValor):
        self.__nombre = nombreValor

    @property
    def codigo(self):
        return self.__codigo
    
    @codigo.setter
    def codigo(self,codigoValor):
        self.__codigo = codigoValor

    @property
    def cod_postal(self):
        return self.__cod_postal
    
    @cod_postal.setter
    def cod_postal(self,codigoPostal):
        self.__cod_postal = codigoPostal

    @property
    def fecha_alta(self):
        return self.__fecha_alta
    
    def __str__(self) -> str:
        return
    
    def __str__(self) -> str:
        return f"nombre{self.__nombre} codigo {self.__codigo} codigo postal{self.__cod_postal} fecha {self.__fecha_alta}"
    

    