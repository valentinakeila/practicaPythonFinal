class Titulo:
    def __init__(self, nombre:str, codigo: int) -> None:
        self.__nombre = nombre
        self.__codigo = codigo


    @property
    def nombre(self):
        return self.__nombre
    @nombre.setter
    def nombre(self, nombre1):
        self.__nombre = nombre1

    @property
    def codigo(self):
        return self.__codigo
    @codigo.setter
    def codigo(self, codigo1):
        self.__codigo = codigo1

    def __str__(self) -> str:
        return f"nombre titulo {self.__nombre} codigo: {self.__codigo}"
    

    