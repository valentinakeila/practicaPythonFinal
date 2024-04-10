class Cliente:
    def __init__(self, nombre:str, apellido:str, nro_documento: str, nro_comunidad: int = None) -> None:
        self.__nombre = nombre
        self.__apellido = apellido
        self.__nro_documento = nro_documento
        self.__nro_comunidad = nro_comunidad


    @property
    def nombre(self):
        return self.__nombre
    
    @nombre.setter
    def nombre(self,nombre1):
        self.__nombre = nombre1

    @property
    def apellido(self):
        return self.__apellido
    
    @apellido.setter
    def apellido(self,apellido1):
        self.__apellido = apellido1


    @property
    def nro_documento(self):
        return self.__nro_documento
    
    @nro_documento.setter
    def nro_documento(self,nro_documento1):
        self.__nro_documento= nro_documento1

    @property
    def nro_comunidad(self):
        return self.__nro_comunidad
    
    @nro_comunidad.setter
    def nro_comunidad(self,nro_comunidad1):
        self.__nro_comunidad= nro_comunidad1


        


    


    