class Titulo:
    def __init__(self, nombre: str, universidad: str) -> None:
        self.__nombre  = nombre
        self.__universidad = universidad


    @property
    def nombre(self):
        return self.__nombre
    
    @nombre.setter
    def nombre(self, nombre1):
        self.__nombre = nombre1

    @property
    def universidad(self):
        return self.__universidad
    
    @universidad.setter
    def universidad(self, universidad1):
        self.__universidad = universidad1


    def __str__(self) -> str:
        return f"nombre: {self.__nombre} universidad: {self.__universidad}"
