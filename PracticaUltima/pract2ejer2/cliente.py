from datetime import *
class Cliente:
    prox_num_cliente = int(0)
    def __init__(self, nombre_apellido:str, direccion:str):
        self.__nombre_apellido = nombre_apellido
        self.__direccion = direccion
        self.__fecha_alta = datetime.today()
        self.__fecha_baja = None
        self.__nro_cliente = Cliente.get_nro_cliente()

    @property
    def nombre_apellido(self):
        return self.__nombre_apellido
    
    @nombre_apellido.setter
    def nombre_apellido(self,nombreApellido):
        self.__nombre_apellido = nombreApellido


    @property
    def direccion(self):
        return self.__direccion
    
    @direccion.setter
    def direccion(self,direccion1):
        self.__direccion = direccion1

    @property
    def fecha_alta(self):
        return self.__fecha_alta
    
    @property
    def fecha_baja(self):
        return self.__fecha_baja
    
    @fecha_baja.setter
    def fecha_baja(self, fechaBaja):
        self.__fecha_baja = fechaBaja

    @property
    def nro_cliente(self):
        return self.__nro_cliente

    

    def eliminar_cliente(self):
        self.__fecha_baja = datetime.today()

    def reactivar_cliente(self):
        self.__fecha_baja = None
        

    @classmethod
    def get_nro_cliente(cls):
        cls.prox_num_cliente += 1
        return cls.prox_num_cliente
    
    def __str__(self) -> str:
        return f"nombre: {self.__nombre_apellido} direccion {self.__direccion}  nro: {self.__nro_cliente}"

