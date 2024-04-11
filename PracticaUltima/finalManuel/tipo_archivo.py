class TipoArchivo:
    def __init__(self, nombre:str,extension_archivo:str) -> None:
        self.__nombre = nombre
        self.__extension_archivo = extension_archivo

    
    @property
    def nombre(self):
        return self.__nombre
    
    @nombre.setter
    def nombre(self,nombre1): 
        self.__nombre = nombre1

    @property
    def extension_archivo(self):
        return self.__extension_archivo
    
    @extension_archivo.setter
    def extension_archivo(self,extension_archivo1):
        self.__extension_archivo = extension_archivo1

    