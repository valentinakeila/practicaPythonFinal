class Tag:
    def __init__(self, nombre:str) -> None:
        self.__nombre =  nombre

    @property
    def nombre(self):
        return self.__nombre
    
    @nombre.setter
    def nombre(self, nombre1):
        self.__nombre = nombre1
    

    def __str__(self) -> str:
        return f"nombre {self.__nombre}"