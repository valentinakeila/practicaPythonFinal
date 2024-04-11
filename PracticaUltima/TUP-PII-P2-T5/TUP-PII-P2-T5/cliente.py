class Cliente:
    def __init__(self, nombre:str,apellido:str, cod_postal:int) -> None:
        self.__nombre = nombre
        self.__apellido = apellido
        self.__cod_postal = cod_postal


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
    def cod_postal(self):
        return self.__cod_postal
    
    @cod_postal.setter
    def cod_postal(self, cod_postal1):
        self.__cod_postal = cod_postal1



    